import copy

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from data_play.main.helper.searchdata import SearchAndReplaceData


def handle_mappings(input_data, mappings, info_data):
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
        include_search_pattern = mapping.get_include_search_pattern()
        replace_with = mapping.get_replace_with()
        if not include_search_pattern or not replace_with:
            continue
        if include_search_pattern in output_data:
            output_data = output_data.replace(include_search_pattern, replace_with)
    return output_data


def process_data(data, meta_data, info_data, flip_output=False):
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
    res = handle_mappings(input_data=input_data, mappings=content_mappings, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res
    # Handle Name Mappings
    if input_File_path:
        res = handle_mappings(input_data=input_File_path, mappings=name_mappings, info_data=info_data)
        meta_data.output_file_path = res
