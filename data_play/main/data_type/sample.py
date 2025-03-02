from collections import OrderedDict

from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.helper.data import Data


# Data has to be declared in global, so that it can be used by other classes

class Sample(DataTypeMaster):

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

    def __init__(self):
        super().__init__()

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

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_content_mappings(self):
        content_mappings = None
        super().set_content_mappings(content_mappings)

    def set_name_mappings(self):
        name_mappings = None
        super().set_name_mappings(name_mappings)

    def set_data_pool(self):
        multi_line_data = """Quick zephyrs blow, vexing daft Jim.
Bright vixens jump; dozy fowl quack.
John quickly extemporized five tow bags.
By Jove, my quick study of lexicography won a prize!"""

        data_pool = [
            #
            Data(
                remarks='Single Line Data; Dictionary',
                input_data='The quick brown fox jumps over the lazy dog',
                content_mappings=[
                    {'brown': 'black'},
                    {'dog': 'cat'},
                ]
            ),
            #
            Data(
                remarks='Multi line Data; Dictionary',
                input_data=multi_line_data,
                content_mappings=[
                    {'quick': 'fast'},
                    {'s': 'SSS'},
                ]
            ),
            #
            Data(
                remarks='Multi line Data; Detailed Dictionary',
                input_data=multi_line_data,
                content_mappings=[
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: 'quick',
                        PhKeys.REPLACE_WITH: 'fast',
                    },
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: 's',
                        PhKeys.REPLACE_WITH: 'SSS',
                    },
                ]
            ),
            #
            Data(
                remarks='Hex Data; Dictionary',
                input_data='8602010287020102',
                content_mappings=[
                    {'02': '22'},
                ]
            ),
            #
            Data(
                remarks='Hex Data; Detailed Dictionary',
                input_data='8602010287020102',
                content_mappings=[
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: '02',
                        PhKeys.REPLACE_WITH: '22',
                    },
                ]
            ),
            #
        ]
        super().set_data_pool(data_pool)
