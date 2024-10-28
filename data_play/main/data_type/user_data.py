from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.helper.data import Data
from data_play.main.helper.searchdata import SearchAndReplaceData


class UserData(DataTypeMaster):

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
                remarks='Simple Data Provided in Text',
                input_data='86020102',
                content_mappings=[
                    SearchAndReplaceData(include_search_pattern='02', replace_with='22'),
                ]
            ),
        ]
        super().set_data_pool(data_pool)
