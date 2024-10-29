from data_play.main.helper.search_patterns import SearchPatterns
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes


class Defaults:
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    QUITE_MODE = False
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    CONTENT_MAPPINGS = PhConstants.LIST_EMPTY
    NAME_MAPPINGS = PhConstants.LIST_EMPTY
    SEARCH_PATTERN = PhConstants.STR_EMPTY
    SEARCH_PATTERN_TYPE = SearchPatterns.NORMAL
    ENCODING = None
    ENCODING_ERRORS = None
