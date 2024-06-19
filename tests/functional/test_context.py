from pangocffi import Context, FontDescription, Gravity, GravityHint, ffi, Font
import unittest

from tests.context_creator import ContextCreator


class TestContext(unittest.TestCase):

    def test_context_init_identical_context(self):
        context = Context()
        identical_context = Context.from_pointer(context.pointer)
        assert identical_context == context

    def test_layout_not_implemented_equality(self):
        context = Context()
        assert ('not an object' != context)

    def test_context_returns_null_from_null_pointer(self):
        with self.assertRaises(ValueError):
            Context.from_pointer(ffi.NULL)

    def test_context_properties(self):
        context = Context()

        desc = FontDescription()
        desc.family = 'sans-serif'
        context.font_description = desc
        assert context.font_description.family == 'sans-serif'

        context.base_gravity = Gravity.EAST
        assert context.base_gravity == Gravity.EAST
        assert context.gravity == Gravity.EAST

        context.gravity_hint = GravityHint.STRONG
        assert context.gravity_hint == GravityHint.STRONG

    def test_context_load_font_none(self):
        context = Context()

        desc = FontDescription()
        desc.family = 'sans-serif'
        font = context.load_font(desc)
        assert font is None

    def test_context_load_font_with_context(self):
        # Setup
        surface_context = ContextCreator.create_surface_without_output()
        context = surface_context.get_pango_context_as_class()

        desc = FontDescription()
        desc.family = 'sans-serif'
        font = context.load_font(desc)
        assert isinstance(font, Font)

        # Tear down
        surface_context.close()
