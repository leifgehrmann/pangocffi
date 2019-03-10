from pangocffi import Layout, LayoutIterator, LayoutRun, ffi
from .context_creator import create_pango_context
import unittest


class TestLayoutRun(unittest.TestCase):

    def test_layout_run_from_pointer(self):
        layout = Layout(create_pango_context())
        layout.set_text('Hello World')
        layout_iter = LayoutIterator(layout)

        layout_run = layout_iter.get_run()
        same_layout = LayoutRun.from_pointer(layout_run.get_pointer())

        assert isinstance(same_layout, LayoutRun)

    def test_layout_run_from_null_pointer(self):
        with self.assertRaises(ValueError):
            LayoutRun.from_pointer(ffi.NULL)

    def test_layout_run_num_chars(self):
        layout = Layout(create_pango_context())
        layout.set_text('Hello World')
        layout_iter = LayoutIterator(layout)

        layout_run = layout_iter.get_run()
        num_chars = layout_run.get_num_chars()

        assert num_chars == 11
