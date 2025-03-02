import copy
import re

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from data_play.main.helper.searchdata import SearchAndReplaceData


def handle_data(data, meta_data, info_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param info_data:
    :param flip_output:
    :return:
    """
    input_data = data.input_data
    input_File_path = meta_data.input_data_org if meta_data.input_mode_key == PhKeys.INPUT_FILE else None
    content_mappings = data.content_mappings
    name_mappings = data.name_mappings
    # input_format = data.input_format
    # output_format = data.output_format
    # if flip_output is True:
    #     input_data = meta_data.parsed_data
    #     input_format = data.output_format
    #     output_format = data.input_format
    # parse_only = True
    # asn1_element = data.asn1_element
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    # Handle Content Mappings
    res = __handle_data(input_data=input_data, mappings=content_mappings, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res
    # Handle Name Mappings
    if input_File_path:
        res = __handle_data(input_data=input_File_path, mappings=name_mappings, info_data=info_data)
        meta_data.output_file_path = res


def __handle_data(input_data, mappings, info_data):
    """

    :param input_data:
    :param mappings:
    :return:
    """
    if PhUtil.is_empty(input_data):
        return input_data
    output_data = copy.deepcopy(input_data)
    for mapping in mappings:
        if isinstance(mapping, dict):
            if len(mapping) == 1:
                # Shorthand is provided
                for key, value in mapping.items():
                    mapping = SearchAndReplaceData(include_search_pattern=key, replace_with=value)
            else:
                mapping = SearchAndReplaceData(**mapping)
        if not isinstance(mapping, SearchAndReplaceData):
            raise ValueError('Unsupported Mapping Provided...')
        start_block = mapping.include_start_block_pattern
        blocks_available = True if PhUtil.is_not_empty(start_block) else False
        include_search_pattern = mapping.get_include_search_pattern()
        if not include_search_pattern:
            continue
        if matching_data(output_data, mapping):
            if blocks_available:
                capture_block = False if PhUtil.is_empty(mapping.delete_block) else True
                if capture_block:
                    if len(mapping.include_start_block_pattern) == 1:
                        # Single character
                        output_data = handle_blocks_w_capture_nested(output_data, mapping)
                    else:
                        output_data = handle_blocks_w_capture(output_data, mapping)
                else:
                    output_data = handle_blocks(output_data, mapping)
            else:
                output_data = replace_data(output_data, mapping)
    return output_data


def find_offset_of_next_block(temp, top_level_only=True,
                              start_char=PhConstants.STR_CURLY_BRACE_START, end_char=PhConstants.STR_CURLY_BRACE_END):
    """

    :param temp:
    :param top_level_only:
    :param start_char:
    :param end_char:
    :return:
    """
    next_offset = find_offset_of_block(temp, start_char, end_char) + 1
    print('next_offset', next_offset)
    # There could be n white spaces (\n, \r , or both)
    next_offset = find_offset_of_next_non_white_space_char(temp, next_offset)
    print('next_offset', next_offset)
    return next_offset


def find_offset_of_block(data, char_to_find, corresponding_char_to_find, parent_only=True):
    """
    Considering Ideal Scenario: Any target char is not present as a comment
    Data Pattern is correct, target characters are available in pairs

    :param data:
    :param char_to_find:
    :param corresponding_char_to_find:
    :return:
    """
    slack = []
    start_char_list = [m.start() for m in re.finditer(char_to_find, data)]
    end_char_list = [m.start() for m in re.finditer(corresponding_char_to_find, data)]
    start_char_list_len = len(start_char_list)
    end_char_list_len = len(end_char_list)
    print('start_char_list', start_char_list)
    print('end_char_list', end_char_list)
    print('start_char_list_len', start_char_list_len)
    print('end_char_list_len', end_char_list_len)
    index_start_char = 0
    index_end_char = 0
    count = 0
    end_char = len(data)  # assignment is needed for the wrong case when target chars are not present
    while count < start_char_list_len + end_char_list_len:
        count += 1
        start_char = int(start_char_list[index_start_char]) if index_start_char < start_char_list_len else -1
        end_char = int(end_char_list[index_end_char]) if index_end_char < end_char_list_len else -1
        if start_char < end_char and start_char != -1:
            # print('pushed', start_char)
            index_start_char += 1
            slack.append(start_char)
        else:
            # print('poped', end_char)
            index_end_char += 1
            if len(slack) == 0:
                additional_data = [
                    f'Corresponding character "{corresponding_char_to_find}" (Total Count {start_char_list_len}) for "{char_to_find}" (Total Count {end_char_list_len}) is not found.',
                    PhUtil.get_key_value_pair('data', data)
                ]
                raise ValueError(PhExceptionHelper(msg_key=PhConstants.INPUT_DATA_ASN1_FORMATION_ISSUE,
                                                   additional_msgs_list=additional_data,
                                                   function_name='find_offset_of_section'))
            slack.pop()
        if len(slack) == 0:
            # print(corresponding_char_to_find, end_char)
            break;
    return end_char


def find_offset_of_next_non_white_space_char(temp, current_offset):
    new_offset = current_offset
    for a in temp[current_offset:]:
        if not a.isspace():
            break
        new_offset += 1
    return new_offset


def handle_blocks(input_data, mapping):
    input_data_list = input_data.split('\n')
    output_data_list = []
    start_block = None
    for _input_data in input_data_list:
        if matching_data_block(_input_data, mapping, PhConstants.START_BLOCK):
            start_block = True
        if matching_data(_input_data, mapping) and start_block:
            _input_data = replace_data(_input_data, mapping)
        if matching_data_block(_input_data, mapping, PhConstants.END_BLOCK):
            start_block = False
        output_data_list.append(_input_data)
    return '\n'.join(output_data_list)


def handle_blocks_w_capture_nested(input_data, mapping):
    offset = 0
    while offset < len(input_data):
        temp = input_data[offset:]
        print(f'len temp: {len(temp)}')
        next_offset = find_offset_of_next_block(temp, top_level_only=False)
        offset += next_offset

    # output_data_list = []
    # output_data_block_list = []
    # start_block = None
    # search_pattern_found = False
    # for input_data in input_data_list:
    #     if matching_data_block(input_data, mapping, PhConstants.START_BLOCK):
    #         if start_block is not True:
    #             search_pattern_found = False
    #         start_block = True
    #     if matching_data(input_data, mapping) and start_block:
    #         search_pattern_found = True
    #         input_data = replace_data(input_data, mapping)
    #     if matching_data_block(input_data, mapping, PhConstants.END_BLOCK):
    #         start_block = False
    #         known_block = True if search_pattern_found else False
    #         output_data_block_list.append(input_data)
    #         if mapping.delete_block == PhConstants.KNOWN and known_block:
    #             output_data_block_list = []
    #         if mapping.delete_block == PhConstants.UNKNOWN and known_block is False:
    #             output_data_block_list = []
    #         output_data_list.append(output_data_block_list.copy())
    #         output_data_block_list = []
    #         continue
    #     if start_block:
    #         output_data_block_list.append(input_data)
    #     else:
    #         output_data_list.append(input_data)
    # return ''.join(PhUtil.normalise_list(output_data_list))


def handle_blocks_w_capture(input_data_str, mapping):
    input_data_list = input_data_str.split('\n')
    output_data_list = []
    output_data_block_list = []
    start_block = None
    search_pattern_found = False
    for input_data in input_data_list:
        if matching_data_block(input_data, mapping, PhConstants.START_BLOCK):
            if start_block is not True:
                search_pattern_found = False
            start_block = True
        if matching_data(input_data, mapping) and start_block:
            search_pattern_found = True
            input_data = replace_data(input_data, mapping)
        if matching_data_block(input_data, mapping, PhConstants.END_BLOCK):
            start_block = False
            known_block = True if search_pattern_found else False
            output_data_block_list.append(input_data)
            if mapping.delete_block == PhConstants.KNOWN and known_block:
                output_data_block_list = []
            if mapping.delete_block == PhConstants.UNKNOWN and known_block is False:
                output_data_block_list = []
            output_data_list.append(output_data_block_list.copy())
            output_data_block_list = []
            continue
        if start_block:
            output_data_block_list.append(input_data)
        else:
            output_data_list.append(input_data)
    return ''.join(PhUtil.normalise_list(output_data_list))


def replace_data(input_data, mapping):
    if mapping.replace_with:
        input_data = input_data.replace(mapping.include_search_pattern, mapping.replace_with)
    return input_data


def matching_data(input_data, mapping):
    res = False
    if mapping.include_search_pattern in input_data:
        res = True
    if '\n' not in input_data:
        # exclude a pattern in the same line?
        if mapping.exclude_search_pattern and mapping.exclude_search_pattern in input_data:
            res = False
    return res


def matching_data_block(input_data, mapping, block):
    res = False
    if block == PhConstants.START_BLOCK:
        if mapping.include_start_block_pattern in input_data:
            res = True
        if mapping.exclude_start_block_pattern and mapping.exclude_start_block_pattern in input_data:
            res = False
    if block == PhConstants.END_BLOCK:
        if mapping.include_end_block_pattern in input_data:
            res = True
        if mapping.exclude_end_block_pattern and mapping.exclude_end_block_pattern in input_data:
            res = False
    return res
