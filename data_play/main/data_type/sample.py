from collections import OrderedDict

from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.helper.data import Data
from data_play.main.helper.folders import Folders
from data_play.main.helper.searchdata import SearchAndReplaceData
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


class Sample(DataTypeMaster):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_content_mappings(self):
        content_mappings = None
        super().set_content_mappings(content_mappings)

    def set_name_mappings(self):
        name_mappings = None
        super().set_name_mappings(name_mappings)

    def set_one_liner(self):
        one_liner = None
        super().set_one_liner(one_liner)

    def set_non_tlv_neighbor(self):
        non_tlv_neighbor = None
        super().set_non_tlv_neighbor(non_tlv_neighbor)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='Miscellaneous Files; SearchAndReplaceData Object',
                input_data=Folders.in_user_gen(),
                content_mappings=[
                    SearchAndReplaceData(include_search_pattern='Copy ', replace_with='Paste '),
                    SearchAndReplaceData(include_search_pattern='"title"', replace_with='"sir_name"'),
                    SearchAndReplaceData(),
                ],
                name_mappings=[
                    SearchAndReplaceData(include_search_pattern='Generic', replace_with='Generic_output'),
                    SearchAndReplaceData(include_search_pattern='1', replace_with='11'),
                    SearchAndReplaceData(include_search_pattern='2', replace_with='22'),
                ]
            ),
            #
            Data(
                remarks='Miscellaneous Files; Dictionary',
                input_data=Folders.in_user_gen(),
                content_mappings=[
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: 'Copy ',
                        PhKeys.REPLACE_WITH: 'Paste ',
                    },
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: '"title"',
                        PhKeys.REPLACE_WITH: '"sir_name"',
                    },
                    {
                    },
                ],
                name_mappings=[
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: 'Generic',
                        PhKeys.REPLACE_WITH: 'Generic_output_dic',
                    },
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: '1',
                        PhKeys.REPLACE_WITH: '11',
                    },
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: '2',
                        PhKeys.REPLACE_WITH: '22',
                    },
                ]
            )
        ]
        super().set_data_pool(data_pool)

    def get_sample_data_pool_for_web(self):
        if not self.data_pool:
            self.set_data_pool()
        sample_data_dic = OrderedDict()
        for data in self.data_pool:
            remarks = data.remarks
            remarks = PhUtil.to_list(remarks, all_str=True, trim_data=True)
            if len(remarks) < 1:
                raise ValueError("Remarks should not be empty")
            key, data.data_group = PhUtil.generate_key_and_data_group(remarks)
            if key in sample_data_dic:
                raise ValueError(f'Duplicate Sample Remarks: {key}')
            sample_data_dic.update({key: super().to_dic(data)})
        return sample_data_dic
