from pangocffi import (
    TabArray, TabAlign
)
import unittest


class TestTabArray(unittest.TestCase):
    def test_identity(self):
        tabarray = TabArray()
        assert len(tabarray) == 0
        tabs = [(TabAlign.LEFT, 1), (TabAlign.LEFT, 10)]
        tabarray.tabs = tabs
        assert len(tabarray) == len(tabs)
        assert tabarray.tabs == tabs

        decimal_point = [':', ',']
        tabarray.decimal_point = decimal_point
        assert tabarray.decimal_point == decimal_point

        assert tabarray.positions_in_pixels is False
        tabarray.positions_in_pixels = True
        assert tabarray.positions_in_pixels is True

    def test_zero_size(self):
        tabarray = TabArray()
        assert len(tabarray) == 0
        assert tabarray.tabs == []

    def test_decimal_point_none(self):
        tabarray = TabArray()

        tabs = [(TabAlign.LEFT, 1), (TabAlign.LEFT, 10)]
        tabarray.tabs = tabs
        decimal_point = [None, None]
        tabarray.decimal_point = decimal_point
        assert tabarray.decimal_point == decimal_point
