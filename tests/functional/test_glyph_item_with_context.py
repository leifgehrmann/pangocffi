from pangocffi import Layout
from .context_creator import create_pango_context
import unittest


class TestGlyphItemIter(unittest.TestCase):

    def test_glyph_item_copies(self):
        text = 'Hi from Παν語'
        layout = Layout(create_pango_context())
        layout.set_text(text)
        layout_iter = layout.get_iter()
        layout_run = layout_iter.get_run()

        assert layout_run.copy().get_pointer() != layout_run.get_pointer()

    def test_glyph_item_splits(self):
        text = 'Hi from Παν語'
        layout = Layout(create_pango_context())
        layout.set_text(text)
        layout_iter = layout.get_iter()
        layout_run = layout_iter.get_run()
        layout_run_hi = layout_run.split(text, 3)

        # "Hi "
        assert layout_run_hi.item.num_chars == 3
        assert layout_run_hi.item.offset == 0

        # "from "
        assert layout_run.item.num_chars == 5
        assert layout_run.item.offset == 3

    def test_glyph_item_get_logical_widths(self):
        text = 'Hi from Παν語'
        layout = Layout(create_pango_context())
        layout.set_text(text)
        layout_iter = layout.get_iter()
        layout_run = layout_iter.get_run()
        logical_widths = layout_run.get_logical_widths(text)

        self.assertListEqual(
            logical_widths,
            [11832, 4552, 4096, 5456, 5456, 8192, 12744, 4096]
        )
