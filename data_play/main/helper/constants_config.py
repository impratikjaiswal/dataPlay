from data_play._git_info import GIT_SUMMARY
from data_play._tool_name import TOOL_NAME
from data_play._version import __version__


class ConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = 'Data Play'
    TOOL_GIT_SUMMARY = GIT_SUMMARY
    TOOL_DESCRIPTION = f'.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, '
    TOOL_URL = 'https://github.com/impratikjaiswal/dataPlay'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/dataPlay/issues'
