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

        layout.text = 'Hi from Παν語'
        assert layout.text == 'Hi from Παν語'

        layout.apply_markup('<span font="italic 30">Hello from Παν語</span>')
        assert layout.text == 'Hello from Παν語'

    def test_layout_setting_properties(self):
        layout = Layout(self.pango_context)

        layout.width = 300
        assert layout.width == 300

        layout.height = 400
        assert layout.height == 400

        assert layout.spacing == 0
        layout.spacing = 30
        assert layout.spacing == 30

        layout.alignment = Alignment.CENTER
        assert layout.alignment is Alignment.CENTER

        layout.ellipsize = EllipsizeMode.MIDDLE
        assert layout.ellipsize is EllipsizeMode.MIDDLE

        layout.wrap = WrapMode.WORD_CHAR
        assert layout.wrap is WrapMode.WORD_CHAR

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
