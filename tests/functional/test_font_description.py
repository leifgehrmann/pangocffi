from pangocffi import FontDescription
from pangocffi import Gravity, Stretch, Style, Variant, Weight, ffi
import unittest


class TestFontDescription(unittest.TestCase):

    def test_font_description_init_identical(self):
        desc = FontDescription()
        identical_desc = desc.from_pointer(desc.pointer)
        assert identical_desc == desc

    def test_font_description_not_implemented_equality(self):
        desc = FontDescription()
        assert ('not an object' != desc)

    def test_font_description_returns_null_from_null_pointer(self):
        with self.assertRaises(ValueError):
            FontDescription.from_pointer(ffi.NULL)

    def test_setting_properties(self):
        desc = FontDescription()

        assert desc.family is None
        desc.family = 'sans-serif'
        assert desc.family == 'sans-serif'

        desc.style = Style.NORMAL
        assert desc.style == Style.NORMAL

        desc.variant = Variant.NORMAL
        assert desc.variant == Variant.NORMAL

        desc.weight = 700
        assert desc.weight == 700
        desc.weight = Weight.BOOK
        assert desc.weight == Weight.BOOK.value

        desc.stretch = Stretch.NORMAL
        assert desc.stretch == Stretch.NORMAL

        desc.size = 123
        assert desc.size == 123
        assert not desc.size_is_absolute

        desc.set_absolute_size(1.23)
        assert desc.size != 123
        assert desc.size_is_absolute

        desc.gravity = Gravity.EAST
        assert desc.gravity == Gravity.EAST
