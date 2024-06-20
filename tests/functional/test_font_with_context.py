from pangocffi import FontDescription, Language, FontMetrics
from ..context_creator import ContextCreator
import unittest


class TestFontWithContext(unittest.TestCase):

    def setUp(self):
        self.context = ContextCreator.create_surface_without_output()
        self.pango_context = self.context.get_pango_context_as_class()

    def tearDown(self):
        self.pango_context = None
        self.context.close()

    def test_get_metrics_without_language(self):
        desc = FontDescription()
        desc.family = 'sans-serif'
        font = self.pango_context.load_font(desc)
        metrics = font.get_metrics()
        assert isinstance(metrics, FontMetrics)
        assert metrics.height > 0

    def test_get_metrics_with_language(self):
        lang = Language.from_string('pt_BR')
        desc = FontDescription()
        desc.family = 'sans-serif'
        font = self.pango_context.load_font(desc)
        metrics = font.get_metrics(lang)
        assert isinstance(metrics, FontMetrics)
        assert metrics.height > 0
