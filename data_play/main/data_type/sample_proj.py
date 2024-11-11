from python_helpers.ph_keys import PhKeys

from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.helper.data import Data


class SampleProj(DataTypeMaster):

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
        """

        :return:
        """
        """
        Rules to handle
        # param delete_empty_lines: After replacement & trim; If the whole line is empty then delete it 
        # param condition: conditional Replacement; evaluate condition
        # may add data or remove data (multi line)
        ## e.g.: HCS; Different ICS are added based on certain condition in multiple files  
        """
        sample_proj_content_mapping = [
            {

                'custom_param01 = None': '',
                'custom_param02 = None': '',
                'custom_param03 = None': '',
                'custom_param04 = None': '',
                'custom_param05 = None': '',
                'custom_param06 = None': '',
                'custom_param07 = None': '',
                'custom_param08 = None': '',
                'custom_param09 = None': '',
                'custom_param10 = None': '',
            },
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: 'custom_param1',
                PhKeys.REPLACE_WITH: '',
            },
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: 's',
                PhKeys.REPLACE_WITH: 'SSS',
            },
        ]

        sample_proj_name_mapping = [
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: '1',
                PhKeys.REPLACE_WITH: '11',
            },
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: '2',
                PhKeys.REPLACE_WITH: '22',
            },
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: '5',
                PhKeys.REPLACE_WITH: 'dataPlay',
            },
        ]

        data_pool = [
            #
            Data(
                remarks='Sample Proj Generator',
                input_data=r'',
                content_mappings=sample_proj_content_mapping,
                name_mappings=sample_proj_name_mapping,
            ),
            #
        ]
        super().set_data_pool(data_pool)
