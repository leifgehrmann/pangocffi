from pangocffi import FontDescription, Language
from ..context_creator import ContextCreator
import unittest


class TestFontMetricsWithContext(unittest.TestCase):

    def setUp(self):
        self.context = ContextCreator.create_surface_without_output()
        self.pango_context = self.context.get_pango_context_as_class()

    def tearDown(self):
        self.pango_context = None
        self.context.close()

    def test_properties(self):
        lang = Language.from_string('pt_BR')
        desc = FontDescription()
        desc.family = 'sans-serif'
        font = self.pango_context.load_font(desc)
        metrics = font.get_metrics(lang)

        assert metrics.approximate_char_width >= 0
        assert metrics.approximate_digit_width >= 0
        assert metrics.ascent >= 0
        assert metrics.descent >= 0
        assert metrics.height >= 0
        assert metrics.strikethrough_position >= 0
        assert metrics.strikethrough_thickness >= 0
        assert isinstance(metrics.underline_position, int)
        assert isinstance(metrics.underline_thickness, int)
