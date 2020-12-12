import unittest
import copy
from pangocffi import ffi, FontDescription, Underline, GravityHint
from pangocffi.enums import Stretch, Style, Variant, Weight, Gravity
from pangocffi.rectangle import Rectangle
from pangocffi.attributes import Attribute


class TestLayout(unittest.TestCase):
    def test_different_layout_equality(self):
        a = Attribute.from_size(4)
        # del a
        b = Attribute.from_size(4)
        c = Attribute.from_family("aaaa")
        assert not c == b
        assert a == b

    def test_pointers_identical(self):
        a = Attribute.from_size_absolute(8)
        b = a._pointer
        c = Attribute.from_pointer(b)
        assert a == c
        print(type(c))

    def test_start_index_end_index(self):
        a = Attribute().from_size(8, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        a.start_index = 8
        a.end_index = 10
        assert a.start_index == 8
        assert a.end_index == 10

    def test_wrong_parameter(self):
        with self.assertRaises(AssertionError):
            Attribute.from_style(Weight.BOLD)
            Attribute.from_variant(Style.NORMAL)
            Attribute.from_stretch(Weight.BOLD)
            Attribute.from_weight(Style.OBLIQUE)

            Attribute.from_size("")
            Attribute.from_size_absolute("a")
            Attribute.from_font_desc(1)

            Attribute.from_foreground_color("", 0, 0)
            Attribute.from_foreground_color(0, "", 0)
            Attribute.from_foreground_color(0, 0, "")

            Attribute.from_background_color("", 0, 0)
            Attribute.from_background_color(0, "", 0)
            Attribute.from_background_color(0, 0, "")

            Attribute.from_strikethrough(1)

            Attribute.from_strikethrough_color("", 0, 0)
            Attribute.from_strikethrough_color(0, "", 0)
            Attribute.from_strikethrough_color(0, 0, "")
            Attribute.from_underline(1)

            Attribute.from_underline_color("", 0, 0)
            Attribute.from_underline_color(0, "", 0)
            Attribute.from_underline_color(0, 0, "")

            Attribute.from_shape(0, 0)
            Attribute.from_shape(Rectangle(), 0)

            Attribute.from_scale(True)
            Attribute.from_rise("a")
            Attribute.from_letter_spacing(True)
            Attribute.from_fallback(1)

            Attribute.from_gravity(2)
            Attribute.from_gravity_hints(33)

            Attribute.from_font_features(23)

            Attribute.from_foreground_alpha("str")
            Attribute.from_background_alpha("foo")

            a = Attribute.from_size(2)
            a.start_index = ""
            a.end_index = ""

    def test_attr_returns_null_from_null_pointer(self):
        with self.assertRaises(ValueError):
            Attribute.from_pointer(ffi.NULL)

    def test_from_family(self):
        a = Attribute.from_family("Roboto", 4, 7)
        b = Attribute.from_family("Roboto", 4, 7)
        assert a.start_index == 4
        assert a.end_index == 7
        assert a == b

    def test_from_style(self):
        a = Attribute.from_style(Style.OBLIQUE, 8, 10)
        b = Attribute.from_style(Style.OBLIQUE, 8, 10)
        assert a.start_index == 8
        assert a.end_index == 10
        assert a == b

    def test_from_variant(self):
        a = Attribute.from_variant(Variant.SMALL_CAPS, 2, 10)
        b = Attribute.from_variant(Variant.SMALL_CAPS, 2, 10)
        assert a.start_index == 2
        assert a.end_index == 10
        assert a == b

    def test_from_stretch(self):
        a = Attribute.from_stretch(Stretch.SEMI_CONDENSED, 9, 10)
        b = Attribute.from_stretch(Stretch.SEMI_CONDENSED)
        assert a.start_index == 9
        assert a.end_index == 10
        assert a == b

    def test_from_weight(self):
        a = Attribute.from_weight(Weight.BOOK, 9, 10)
        b = Attribute.from_weight(Weight.BOOK, 9, 10)
        assert a.start_index == 9
        assert a.end_index == 10
        assert a == b

    def test_from_size(self):
        a = Attribute.from_size(5, 9, 10)
        b = Attribute.from_size(5, 9, 10)
        assert a.start_index == 9
        assert a.end_index == 10
        assert a == b

    def test_from_size_absolute(self):
        a = Attribute.from_size_absolute(5, 9, 10)
        b = Attribute.from_size_absolute(5, 9, 10)
        assert a.start_index == 9
        assert a.end_index == 10
        assert a == b

    def test_from_font_desc(self):
        font_desc = FontDescription()
        a = Attribute.from_font_desc(font_desc, 1, 10)
        b = Attribute.from_font_desc(font_desc, 1, 10)
        assert a.start_index == 1
        assert a.end_index == 10
        assert a == b

    def test_from_foreground_color(self):
        a = Attribute.from_foreground_color(5, 1, 10, 5, 6)
        b = Attribute.from_foreground_color(5, 1, 10, 5, 6)
        assert a.start_index == 5
        assert a.end_index == 6
        assert a == b

    def test_from_background_color(self):
        a = Attribute.from_background_color(5, 1, 10, 5, 6)
        b = Attribute.from_background_color(5, 1, 10, 5, 6)
        assert a.start_index == 5
        assert a.end_index == 6
        assert a == b

    def test_from_strikethrough(self):
        a = Attribute.from_strikethrough(True, 5, 6)
        b = Attribute.from_strikethrough(True, 5, 6)
        assert a.start_index == 5
        assert a.end_index == 6
        assert a == b

    def test_from_strikethrough_color(self):
        a = Attribute.from_strikethrough_color(1, 2, 3, 5, 6)
        b = Attribute.from_strikethrough_color(1, 2, 3, 5, 6)
        assert a.start_index == 5
        assert a.end_index == 6
        assert a == b

    def test_from_underline(self):
        a = Attribute.from_underline(Underline.DOUBLE, 5, 6)
        b = Attribute.from_underline(Underline.DOUBLE, 5, 6)
        assert a.start_index == 5
        assert a.end_index == 6
        assert a == b

    def test_from_underline_color(self):
        a = Attribute.from_underline_color(1, 2, 3, 5, 9)
        b = Attribute.from_underline_color(1, 2, 3, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_shape(self):
        d = Rectangle()
        e = Rectangle()
        a = Attribute.from_shape(d, e, 5, 9)
        b = Attribute.from_shape(d, e, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_scale(self):
        a = Attribute.from_scale(3, 5, 9)
        b = Attribute.from_scale(3, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_rise(self):
        a = Attribute.from_rise(3, 5, 9)
        b = Attribute.from_rise(3, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_letter_spacing(self):
        a = Attribute.from_letter_spacing(3, 5, 9)
        b = Attribute.from_letter_spacing(3, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_fallback(self):
        a = Attribute.from_fallback(True, 5, 9)
        b = Attribute.from_fallback(True, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_gravity(self):
        a = Attribute.from_gravity(Gravity.EAST, 5, 9)
        b = Attribute.from_gravity(Gravity.EAST, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_gravity_hints(self):
        a = Attribute.from_gravity_hints(GravityHint.STRONG, 5, 9)
        b = Attribute.from_gravity_hints(GravityHint.STRONG, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_font_features(self):
        a = Attribute.from_font_features("liga=0", 5, 9)
        b = Attribute.from_font_features("liga=0", 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_foreground_alpha(self):
        a = Attribute.from_foreground_alpha(56, 5, 9)
        b = Attribute.from_foreground_alpha(56, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_from_background_alpha(self):
        a = Attribute.from_background_alpha(56, 5, 9)
        b = Attribute.from_background_alpha(56, 5, 9)
        assert a.start_index == 5
        assert a.end_index == 9
        assert a == b

    def test_copy(self):
        a = Attribute.from_background_alpha(56, 5, 9)
        b = copy.copy(a)
        assert a == b
        c = copy.deepcopy(a)
        assert a == c
        with self.assertRaises(NotImplementedError):
            a == 6
