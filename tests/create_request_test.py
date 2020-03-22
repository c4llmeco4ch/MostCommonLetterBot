import pytest


class TestBuildRequest:
    """test different ways to manipulate request string"""

    def test_valid_dates(self):
        """provided valid dates"""
        pass

    def test_invalid_dates(self):
        """provided invalid dates"""
        pass

    def test_valid_langs(self):
        """providing valid langs"""
        pass

    def test_invalid_langs(self):
        """providing invalid langs"""
        pass

    def test_valid_locations(self):
        """providing valid locations"""
        pass

    # Other tests to come


class TestEnglishParse:
    """test reading in english text and parsing for expected letters"""

    def test_normal_string(self):
        """providing regular sentence"""
        pass

    def test_empty_string(self):
        """providing empty string"""
        pass

    def test_mixed_case(self):
        """providing string with mixed cases"""
        pass

    def test_all_caps(self):
        """providing string with all caps"""
        pass

    def test_non_english_chars(self):
        """when language is set to english, non-en characters aren't read"""
        pass


