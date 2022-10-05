from pangocffi import (
    Context,
    FontDescription,
    Layout,
    ffi,
    Attribute,
    AttrList,
)
import unittest


class TestLayout(unittest.TestCase):
    @staticmethod
    def test_layout_returns_identical_context():
        context = Context()
        layout = Layout(context)
        identical_context = layout.context
        assert identical_context.pointer == context.pointer

    @staticmethod
    def test_layout_get_pointer_returns_identical_layout():
        context = Context()
        layout = Layout(context)
        identical_layout = Layout.from_pointer(layout.pointer)
        assert identical_layout.pointer == layout.pointer

    def test_layout_not_implemented_equality(self):
        context = Context()
        layout = Layout(context)
        assert "not an object" != layout

    def test_layout_returns_null_from_null_pointer(self):
        with self.assertRaises(ValueError):
            Layout.from_pointer(ffi.NULL)

    @staticmethod
    def test_layout_setting_font_description():
        context = Context()
        layout = Layout(context)

        # Assert that the font description is not set
        assert layout.font_description is None

        # Creating the font description
        desc = FontDescription()
        desc.family = "sans-serif"
        layout.font_description = desc

        # Verifying the font description was set
        same_desc = layout.font_description
        assert same_desc.family == desc.family

        # Changing the font description
        desc.family = "serif"
        assert same_desc.family != desc.family

        # Resetting the font description
        layout.font_description = None
        assert layout.font_description is None

    @staticmethod
    def test_layout_setting_text():
        context = Context()
        layout = Layout(context)

        layout.width = 300

        layout.text = "Hi from Pango"
        layout.apply_markup('<span font="italic 30">Hi from Παν語</span>')

    def test_set_attributes(self):
        context = Context()
        layout = Layout(context)
        layout.text = "Working?"
        attr = Attribute.from_size(5, 1, 4)
        attr_list = AttrList()

        attr_list.insert(attr)

        layout.attributes = attr_list
        assert layout.attributes is not None

        del layout.attributes
        assert layout.attributes is None

        # Resetting the attributes
        layout.attributes = None
        assert layout.attributes is None
