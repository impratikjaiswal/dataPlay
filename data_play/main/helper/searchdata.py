from data_play.main.helper.defaults import Defaults
from python_helpers.ph_util import PhUtil


class SearchAndReplaceData:
    def __init__(self,
                 include_search_pattern=None,
                 include_search_pattern_is_regex=False,
                 exclude_search_pattern=None,
                 exclude_search_pattern_is_regex=False,
                 replace_with=None,
                 replace_with_is_regex=False,
                 ):
        self.include_search_pattern = PhUtil.set_if_none(include_search_pattern, Defaults.SEARCH_PATTERN)
        self.include_search_pattern_is_regex = PhUtil.set_if_none(include_search_pattern_is_regex,
                                                                  Defaults.SEARCH_PATTERN_TYPE)
        self.exclude_search_pattern = PhUtil.set_if_none(exclude_search_pattern, Defaults.SEARCH_PATTERN)
        self.exclude_search_pattern_is_regex = PhUtil.set_if_none(exclude_search_pattern_is_regex,
                                                                  Defaults.SEARCH_PATTERN_TYPE)
        self.replace_with = PhUtil.set_if_none(replace_with, Defaults.SEARCH_PATTERN)
        self.replace_with_is_regex = PhUtil.set_if_none(replace_with_is_regex, Defaults.SEARCH_PATTERN_TYPE)

    def get_include_search_pattern(self):
        return self.include_search_pattern

    def get_replace_with(self):
        return self.replace_with
