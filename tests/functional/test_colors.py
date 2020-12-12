import copy
import unittest

from pangocffi import Color


class TestLayout(unittest.TestCase):
    def test_init(self):
        Color(5, 5, 5)

    def test_copy(self):
        a = Color(5, 5, 5)
        b = a.copy()
        assert a == b
        c = copy.copy(a)
        assert a == c
        d = copy.deepcopy(a)
        assert a == d

    def test_parse_color(self):
        b = Color(0, 0, 0)
        b.parse_color("#123")
        assert str(b) == "<Color(red=572657937,blue=0,green=13107)>"
        b.red == 572657937
        b.blue == 0
        b.green == 13107

    def test_to_string(self):
        b = Color(0, 0, 0)
        b.parse_color("#123")
        assert b.to_string() == "#111122223333"
