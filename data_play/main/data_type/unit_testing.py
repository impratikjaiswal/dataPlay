import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys

from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.helper.data import Data
from data_play.main.helper.folders import Folders
from data_play.main.helper.searchdata import SearchAndReplaceData


class UnitTesting(DataTypeMaster):

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
        single_line_data = 'The quick brown fox jumps over the lazy dog'

        single_line_data_content_mapping = [
            {'brown': 'black'},
            {'dog': 'cat'},
        ]

        multi_line_data = """Quick zephyrs blow, vexing daft Jim.
        Bright vixens jump; dozy fowl quack.
        John quickly extemporized five tow bags.
        By Jove, my quick study of lexicography won a prize!"""

        multi_line_data_content_mapping = [
            {'quick': 'fast'},
            {'s': 'SSS'},
        ]

        multi_line_data_content_mapping_detailed = [
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: 'quick',
                PhKeys.REPLACE_WITH: 'fast',
            },
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: 's',
                PhKeys.REPLACE_WITH: 'SSS',
            },
        ]

        hex_data = '8602010287020102'

        hex_data_content_mapping = [
            {'02': '22'},
        ]

        hex_data_content_mapping_detailed = [
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: '02',
                PhKeys.REPLACE_WITH: '22',
            },
        ]

        content_mappings_test = [
            {'Copy ': 'Paste '},
            {'"title"': '"sir_name"'},
            {'': ''},
            {'Fantasy': 'Horror'},
            {'svg': 'jpeg'},
            {'SVG': 'PNG'},
        ]

        content_mappings_detailed_test = [
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
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: 'Fantasy',
                PhKeys.REPLACE_WITH: 'Horror',
            },
            {  # TODO:  Currently Case sensitive, so no changes for this
                PhKeys.INCLUDE_SEARCH_PATTERN: 'svg',
                PhKeys.REPLACE_WITH: 'jpeg',
            },
            {
                PhKeys.INCLUDE_SEARCH_PATTERN: 'SVG',
                PhKeys.REPLACE_WITH: 'PNG',
            },
        ]

        content_mappings_search_n_replace_test = [
            SearchAndReplaceData(include_search_pattern='Copy ', replace_with='Paste '),
            SearchAndReplaceData(include_search_pattern='"title"', replace_with='"sir_name"'),
            SearchAndReplaceData(),
            SearchAndReplaceData(include_search_pattern='Fantasy ', replace_with='Horror '),
            # TODO: Currently Case sensitive, so no changes for this
            SearchAndReplaceData(include_search_pattern='svg', replace_with='jpeg'),
            SearchAndReplaceData(include_search_pattern='SVG', replace_with='PNG'),
        ]

        name_mappings_test = [
            {'1': '11'},
            {'2': '22'},
            {'5': 'dataPlay'},
        ]

        name_mappings_detailed_test = [
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

        name_mappings_search_n_replace_test = [
            SearchAndReplaceData(include_search_pattern='1', replace_with='11'),
            SearchAndReplaceData(include_search_pattern='2', replace_with='22'),
            SearchAndReplaceData(include_search_pattern='5', replace_with='dataPlay'),
        ]

        data_pool = [
            #
            Data(
                remarks='Single Line Data; Dictionary',
                input_data=single_line_data,
                content_mappings=single_line_data_content_mapping,
            ),
            #
            Data(
                remarks='Multi line Data; Dictionary',
                input_data=multi_line_data,
                content_mappings=multi_line_data_content_mapping,
            ),
            #
            Data(
                remarks='Multi line Data; Detailed Dictionary',
                input_data=multi_line_data,
                content_mappings=multi_line_data_content_mapping_detailed,
            ),
            #
            Data(
                remarks='Hex Data; Dictionary',
                input_data=hex_data,
                content_mappings=hex_data_content_mapping,
            ),
            #
            Data(
                remarks='List; Dictionary',
                input_data=[hex_data, single_line_data, multi_line_data, hex_data],
                content_mappings=single_line_data_content_mapping + multi_line_data_content_mapping + hex_data_content_mapping_detailed,
            ),
            #
            Data(
                remarks='Hex Data; SearchAndReplaceData Object',
                input_data=hex_data,
                content_mappings=[
                    SearchAndReplaceData(include_search_pattern='02', replace_with='22'),
                ]
            ),
            #
            Data(
                remarks='Miscellaneous Files; Dictionary only content',
                input_data=Folders.in_user_gen(),
                content_mappings=content_mappings_test,
                name_mappings=name_mappings_detailed_test +
                              [
                                  {
                                      PhKeys.INCLUDE_SEARCH_PATTERN: 'Generic',
                                      PhKeys.REPLACE_WITH: os.sep.join(['Generic_Output', 'dic_content']),
                                  },
                              ],
            ),
            #
            Data(
                remarks='Miscellaneous Files; Dictionary; Content & Name',
                input_data=Folders.in_user_gen(),
                content_mappings=content_mappings_test,
                name_mappings=name_mappings_test +
                              [
                                  {
                                      PhKeys.INCLUDE_SEARCH_PATTERN: 'Generic',
                                      PhKeys.REPLACE_WITH: os.sep.join(['Generic_Output', 'dic_content_n_name']),
                                  },
                              ],
            ),
            #
            Data(
                remarks='Miscellaneous Files; Detailed Dictionary',
                input_data=Folders.in_user_gen(),
                content_mappings=content_mappings_detailed_test,
                name_mappings=name_mappings_detailed_test +
                              [
                                  {
                                      PhKeys.INCLUDE_SEARCH_PATTERN: 'Generic',
                                      PhKeys.REPLACE_WITH: os.sep.join(['Generic_Output', 'detailed_dic']),
                                  },
                              ],
            ),
            #
            Data(
                remarks='Miscellaneous Files; SearchAndReplaceData Object',
                input_data=Folders.in_user_gen(),
                content_mappings=content_mappings_search_n_replace_test,
                name_mappings=name_mappings_search_n_replace_test + [
                    SearchAndReplaceData(include_search_pattern='Generic',
                                         replace_with=os.sep.join(['Generic_Output', 'SearchAndReplaceData'])
                                         ),
                ],
            ),
            #
            Data(
                remarks='Miscellaneous Files; Detailed Dictionary; Encoding UTF8',
                input_data=Folders.in_user_gen(),
                content_mappings=content_mappings_detailed_test,
                name_mappings=name_mappings_detailed_test +
                              [
                                  {
                                      PhKeys.INCLUDE_SEARCH_PATTERN: 'Generic',
                                      PhKeys.REPLACE_WITH: os.sep.join(['Generic_Output', 'detailed_dic_encoding']),
                                  },
                              ],
                encoding=PhConstants.CHAR_ENCODING_UTF8,
                encoding_errors=PhConstants.CHAR_ENCODING_ERRORS_REPLACE,
            ),
            #
        ]
        super().set_data_pool(data_pool)
