from data_play.main.helper.constants import Constants
from data_play.main.helper.data import Data
from data_play.main.helper.defaults import Defaults
from data_play.main.helper.keywords import KeyWords
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


def print_data(data=None, meta_data=None, info_data=None, master_data=None):
    """
    
    :param data:
    :param meta_data:
    :param info_data:
    :param master_data:
    :return:
    """
    if master_data is not None and isinstance(master_data, PhMasterData):
        data = master_data.get_master_data(PhMasterDataKeys.DATA)
        meta_data = master_data.get_master_data(PhMasterDataKeys.META_DATA)
        info_data = master_data.get_master_data(PhMasterDataKeys.INFO_DATA)
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE
    if data.print_info:
        remarks_original = data.get_remarks_as_str(user_original_remarks=True)
        remarks_generated = data.get_remarks_as_str()
        remarks_generated_stripping_needed = True if remarks_generated.endswith(
            PhConstants.DEFAULT_TRIM_STRING) else False
        if remarks_original:
            if remarks_generated_stripping_needed:
                if remarks_generated.strip(PhConstants.DEFAULT_TRIM_STRING) in remarks_original:
                    remarks_generated = ''
            else:
                if remarks_original in remarks_generated:
                    remarks_generated = ''
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                       remarks_generated))
        if info_data is not None:
            info_count = info_data.get_info_count()
            info_msg = info_data.get_info_str()
            if info_msg:
                sep = PhConstants.SEPERATOR_MULTI_LINE_TABBED if info_count > 1 else PhConstants.SEPERATOR_ONE_LINE
                meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO_DATA, sep, info_msg))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(PhKeys.TRANSACTION_ID, PhConstants.SEPERATOR_ONE_LINE, meta_data.transaction_id,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.ENCODING, PhConstants.SEPERATOR_ONE_LINE, data.encoding,
                                   dic_format=False, print_also=False) if data.encoding else None,
            get_dic_data_and_print(PhKeys.ENCODING_ERRORS, PhConstants.SEPERATOR_ONE_LINE, data.encoding_errors,
                                   dic_format=False, print_also=False) if data.encoding_errors else None,
            get_dic_data_and_print(PhKeys.CONTENT_MAPPINGS, PhConstants.SEPERATOR_ONE_LINE, data.content_mappings,
                                   dic_format=False, print_also=False) if data.content_mappings else None,
            get_dic_data_and_print(PhKeys.NAME_MAPPINGS, PhConstants.SEPERATOR_ONE_LINE, data.name_mappings,
                                   dic_format=False, print_also=False) if data.name_mappings else None,
            get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                   dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, meta_data.input_data_org))
    print_output = data.print_output
    if data.print_output and print_output:  # and meta_data.parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    PhUtil.print_separator()


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    return PhUtil.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # Always exclude output files
    meta_data.excludes = ['*_' + KeyWords.OUTPUT_FILE_NAME_KEYWORD + '.*']
    # Include Everything for now


def parse_config(config_data):
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if not v:
            continue
        if isinstance(v, str):
            # Trim Garbage data
            v = PhUtil.trim_white_spaces_in_str(v)
            v = PhUtil.clear_quotation_marks(v)
            v_lower_case = v.lower()
            v_eval = None
            try:
                v_eval = eval(v)
                if isinstance(v_eval, str):
                    # Everything was already str
                    v_eval = None
            except:
                pass
            if v_lower_case in ['none']:
                v = None
                config_data[k] = v
            if v_lower_case in ['true']:
                v = True
                config_data[k] = v
            if v_lower_case in ['false']:
                v = False
                config_data[k] = v
        if not v:
            continue
        if v in [PhConstants.STR_SELECT_OPTION]:
            v = None
            config_data[k] = v
        if k in [PhKeys.INPUT_DATA]:
            if v_eval is not None:
                v = v_eval
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data before cleaning', verbose=True, depth_level=1)
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_printing(data):
    """

    :param data:
    :return:
    """
    data.quite_mode = PhUtil.set_if_none(data.quite_mode, Defaults.QUITE_MODE)
    data.print_input = PhUtil.set_if_none(data.print_input, Defaults.PRINT_INPUT)
    data.print_output = PhUtil.set_if_none(data.print_output, Defaults.PRINT_OUTPUT)
    data.print_info = PhUtil.set_if_none(data.print_info, Defaults.PRINT_INFO)


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    data.encoding = PhUtil.set_if_none(data.encoding, Defaults.ENCODING)
    data.encoding_errors = PhUtil.set_if_none(data.encoding_errors, Defaults.ENCODING_ERRORS)
    data.content_mappings = PhUtil.set_if_none(data.content_mappings, Defaults.CONTENT_MAPPINGS)
    data.name_mappings = PhUtil.set_if_none(data.name_mappings, Defaults.NAME_MAPPINGS)
    if meta_data is None:
        return


def read_web_request(request_form):
    return Data(**parse_config(request_form))


def read_input_file(data, meta_data, info_data):
    try:
        # Binary File
        with open(data.input_data, mode='r', encoding=data.encoding, errors=data.encoding_errors) as the_file:
            resp = ''.join(the_file.readlines())
    except UnicodeDecodeError:
        # Binary File/
        with open(data.input_data, 'rb') as the_file:
            resp = the_file.read()
    if not resp:
        raise ValueError(PhExceptionHelper(msg_key=Constants.INPUT_FILE_EMPTY))
    return resp


def write_output_file(data, meta_data, info_data):
    data_to_write = meta_data.parsed_data
    data_to_write = PhUtil.set_if_none(data_to_write, PhConstants.STR_EMPTY)
    with open(meta_data.output_file_path, mode='w', encoding=data.encoding, errors=data.encoding_errors) as file:
        file.writelines(data_to_write)
