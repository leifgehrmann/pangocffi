from pangocffi import (
    TabArray, TabAlign
)
import unittest


class TestTabArray(unittest.TestCase):
    def test_identity(self):
        tab_array = TabArray()
        assert len(tab_array) == 0
        tabs = [(TabAlign.LEFT, 1), (TabAlign.LEFT, 10)]
        tab_array.tabs = tabs
        assert len(tab_array) == len(tabs)
        assert tab_array.tabs == tabs

        decimal_point = [':', ',']
        tab_array.decimal_point = decimal_point
        assert tab_array.decimal_point == decimal_point

        assert tab_array.positions_in_pixels is False
        tab_array.positions_in_pixels = True
        assert tab_array.positions_in_pixels is True

    def test_zero_size(self):
        tab_array = TabArray()
        assert len(tab_array) == 0
        assert tab_array.tabs == []

    def test_decimal_point_none(self):
        tab_array = TabArray()

        tabs = [(TabAlign.LEFT, 1), (TabAlign.LEFT, 10)]
        tab_array.tabs = tabs
        decimal_point = [None, None]
        tab_array.decimal_point = decimal_point
        assert tab_array.decimal_point == decimal_point

    def test_decimal_point_index_error(self):
        tab_array = TabArray()

        tab_array.tabs = [(TabAlign.LEFT, 1), (TabAlign.LEFT, 10)]
        with self.assertRaises(IndexError):
            tab_array.decimal_point = [',']
