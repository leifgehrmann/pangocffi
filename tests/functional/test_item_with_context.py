from pangocffi import Layout, ffi
from ..context_creator import ContextCreator
import unittest


class TestItemWithContext(unittest.TestCase):

    def setUp(self):
        self.context = ContextCreator.create_surface_without_output()
        self.pango_context = self.context.get_pango_context_as_class()

    def tearDown(self):
        self.pango_context = None
        self.context.close()

    def test_item_properties(self):
        layout = Layout(self.pango_context)
        layout.text = 'Hi from Παν語'
        layout_iter = layout.get_iter()

        layout_run = layout_iter.get_run()
        layout_run_item = layout_run.item

        assert layout_run_item.length == 8
        assert layout_run_item.offset == 0
        assert layout_run_item.num_chars == 8
        assert isinstance(layout_run_item.pointer, ffi.CData)

        assert layout_iter.next_run()
        layout_run = layout_iter.get_run()
        layout_run_item = layout_run.item

        assert layout_run_item.length == 6
        assert layout_run_item.offset == 8
        assert layout_run_item.num_chars == 3
        assert isinstance(layout_run_item.pointer, ffi.CData)
