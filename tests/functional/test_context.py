from pangocffi import Context, FontDescription, Gravity, GravityHint, ffi
import unittest


class TestContext(unittest.TestCase):

    def test_context_init_identical_context(self):
        context = Context()
        identical_context = Context.from_pointer(context.get_pointer())
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
        assert context.font_description.get_family() == 'sans-serif'

        context.base_gravity = Gravity.EAST
        assert context.base_gravity == Gravity.EAST
        assert context.gravity == Gravity.EAST

        context.gravity_hint = GravityHint.STRONG
        assert context.gravity_hint == GravityHint.STRONG
