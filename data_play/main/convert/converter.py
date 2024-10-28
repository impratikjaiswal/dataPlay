from data_play.main.helper.data import Data
from data_play.main.helper.defaults import Defaults
from data_play.main.helper.keywords import KeyWords
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


def print_data(data=None, meta_data=None, info_data=None, master_data=None):
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
            get_dic_data_and_print(PhKeys.CONTENT_MAPPINGS, PhConstants.SEPERATOR_ONE_LINE, data.content_mappings,
                                   dic_format=False, print_also=False) if data.content_mappings else None,
            get_dic_data_and_print(PhKeys.NAME_MAPPINGS, PhConstants.SEPERATOR_ONE_LINE, data.name_mappings,
                                   dic_format=False, print_also=False) if data.name_mappings else None,
            get_dic_data_and_print(PhKeys.ONE_LINER, PhConstants.SEPERATOR_ONE_LINE, data.one_liner,
                                   dic_format=False, print_also=False) if data.one_liner else None,
            get_dic_data_and_print(PhKeys.NON_TLV_NEIGHBOR, PhConstants.SEPERATOR_ONE_LINE, data.non_tlv_neighbor,
                                   dic_format=False, print_also=False) if data.non_tlv_neighbor else None,
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
    if data.quite_mode is None:
        data.quite_mode = Defaults.QUITE_MODE
    if data.print_input is None:
        data.print_input = Defaults.PRINT_INPUT
    if data.print_output is None:
        data.print_output = Defaults.PRINT_OUTPUT
    if data.print_info is None:
        data.print_info = Defaults.PRINT_INFO


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    if data.content_mappings is None:
        data.content_mappings = Defaults.CONTENT_MAPPINGS
    if data.name_mappings is None:
        data.name_mappings = Defaults.NAME_MAPPINGS
    if data.one_liner is None:
        data.one_liner = Defaults.ONE_LINER
    if data.non_tlv_neighbor is None:
        data.non_tlv_neighbor = Defaults.NON_TLV_NEIGHBOR
    if meta_data is None:
        return


def read_web_request(request_form):
    return Data(**parse_config(request_form))


def set_defaults_individual_params(content_mappings, name_mappings, one_liner, non_tlv_neighbor):
    """
    Set Default Values if nothing is set.

    :param non_tlv_neighbor:
    :param content_mappings:
    :param name_mappings:
    :param one_liner:
    :return:
    """
    if content_mappings is None:
        content_mappings = Defaults.CONTENT_MAPPINGS
    if name_mappings is None:
        name_mappings = Defaults.NAME_MAPPINGS
    if one_liner is None:
        one_liner = Defaults.ONE_LINER
    if one_liner is None:
        non_tlv_neighbor = Defaults.NON_TLV_NEIGHBOR
    return content_mappings, name_mappings, one_liner, non_tlv_neighbor


def write_output_file(output_file_name, parsed_data):
    with open(output_file_name, 'w') as file:
        file.writelines(parsed_data)