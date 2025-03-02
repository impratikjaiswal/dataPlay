from python_helpers.ph_util import PhUtil

from data_play.main.helper.defaults import Defaults


class SearchAndReplaceData:
    def __init__(self,
                 include_search_pattern=None,
                 include_search_pattern_is_regex=False,
                 exclude_search_pattern=None,
                 exclude_search_pattern_is_regex=False,
                 replace_with=None,
                 replace_with_is_regex=False,
                 delete_block=None,
                 block_level=None,
                 include_start_block_pattern=None,
                 include_start_block_pattern_is_regex=None,
                 exclude_start_block_pattern=None,
                 exclude_start_block_pattern_is_regex=None,
                 include_end_block_pattern=None,
                 include_end_block_pattern_is_regex=None,
                 exclude_end_block_pattern=None,
                 exclude_end_block_pattern_is_regex=None,
                 ):
        self.include_search_pattern = PhUtil.set_if_none(include_search_pattern, Defaults.SEARCH_PATTERN)
        self.include_search_pattern_is_regex = PhUtil.set_if_none(include_search_pattern_is_regex,
                                                                  Defaults.SEARCH_PATTERN_TYPE)
        self.exclude_search_pattern = PhUtil.set_if_none(exclude_search_pattern, Defaults.SEARCH_PATTERN)
        self.exclude_search_pattern_is_regex = PhUtil.set_if_none(exclude_search_pattern_is_regex,
                                                                  Defaults.SEARCH_PATTERN_TYPE)
        self.replace_with = PhUtil.set_if_none(replace_with, Defaults.SEARCH_PATTERN)
        self.replace_with_is_regex = PhUtil.set_if_none(replace_with_is_regex, Defaults.SEARCH_PATTERN_TYPE)
        #
        self.delete_block = PhUtil.set_if_none(delete_block)
        self.delete_block = PhUtil.set_if_none(delete_block)
        #
        self.include_start_block_pattern = PhUtil.set_if_none(include_start_block_pattern)
        self.include_start_block_pattern_is_regex = PhUtil.set_if_none(include_start_block_pattern_is_regex,
                                                                       Defaults.SEARCH_PATTERN_TYPE)
        self.exclude_start_block_pattern = PhUtil.set_if_none(exclude_start_block_pattern)
        self.exclude_start_block_pattern_is_regex = PhUtil.set_if_none(exclude_start_block_pattern_is_regex,
                                                                       Defaults.SEARCH_PATTERN_TYPE)
        self.include_end_block_pattern = PhUtil.set_if_none(include_end_block_pattern)
        self.include_end_block_pattern_is_regex = PhUtil.set_if_none(include_end_block_pattern_is_regex,
                                                                     Defaults.SEARCH_PATTERN_TYPE)
        self.exclude_end_block_pattern = PhUtil.set_if_none(exclude_end_block_pattern)
        self.exclude_end_block_pattern_is_regex = PhUtil.set_if_none(exclude_end_block_pattern_is_regex,
                                                                     Defaults.SEARCH_PATTERN_TYPE)

    def get_include_search_pattern(self):
        return self.include_search_pattern

    def get_replace_with(self):
        return self.replace_with
