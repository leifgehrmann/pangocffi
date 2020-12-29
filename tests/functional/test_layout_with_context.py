from pangocffi import Layout, Alignment, EllipsizeMode, WrapMode
from ..context_creator import ContextCreator
import unittest


class TestLayoutWithContext(unittest.TestCase):

    def setUp(self):
        self.context = ContextCreator.create_surface_without_output()
        self.pango_context = self.context.get_pango_context_as_class()

    def tearDown(self):
        self.pango_context = None
        self.context.close()

    def test_layout_setting_text(self):
        layout = Layout(self.pango_context)

        layout.set_text('Hi from Παν語')
        assert layout.get_text() == 'Hi from Παν語'

        layout.set_markup('<span font="italic 30">Hello from Παν語</span>')
        assert layout.get_text() == 'Hello from Παν語'

    def test_layout_setting_properties(self):
        layout = Layout(self.pango_context)

        layout.set_width(300)
        assert layout.get_width() == 300

        layout.set_height(400)
        assert layout.get_height() == 400

        assert layout.get_spacing() == 0
        layout.set_spacing(30)
        assert layout.get_spacing() == 30

        layout.set_alignment(Alignment.CENTER)
        assert layout.get_alignment() is Alignment.CENTER

        layout.set_ellipsize(EllipsizeMode.MIDDLE)
        assert layout.get_ellipsize() is EllipsizeMode.MIDDLE

        layout.set_wrap(WrapMode.WORD_CHAR)
        assert layout.get_wrap() is WrapMode.WORD_CHAR

        ink_rect, logical_rect = layout.get_extents()
        assert logical_rect.width == 0
        # The height of the layout will be the height of the font, despite no
        # text being set against the layout.
        assert logical_rect.height > 0

        width, height = layout.get_size()
        assert width == 0
        # The height of the layout will be the height of the font, despite no
        # text being set against the layout.
        assert height > 0

        baseline = layout.get_baseline()
        # The baseline of the layout will correspond to the selected font,
        # despite no text being set against the layout.
        assert baseline > 0

        line_count = layout.get_line_count()
        assert line_count == 1
