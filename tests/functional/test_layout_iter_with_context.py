from pangocffi import Layout, LayoutIter, Rectangle, ffi
from .context_creator import ContextCreator
import unittest


class TestLayoutIterWithContext(unittest.TestCase):

    def setUp(self):
        self.pango_context = ContextCreator.get_pango_context()

    def tearDown(self):
        self.pango_context = None
        ContextCreator.free()

    def test_layout_iter_pointer(self):
        layout = Layout(self.pango_context)
        layout_iter = layout.get_iter()
        assert isinstance(layout_iter, LayoutIter)
        assert isinstance(layout_iter.get_pointer(), ffi.CData)

        pointer_shallow_copy = layout_iter.get_pointer()
        layout_iter_shallow_copy = LayoutIter.from_pointer(
            pointer_shallow_copy
        )
        assert isinstance(layout_iter_shallow_copy, LayoutIter)
        assert isinstance(layout_iter_shallow_copy.get_pointer(), ffi.CData)

    def test_layout_iter_properties(self):
        layout = Layout(self.pango_context)
        layout_iter = layout.get_iter()

        assert layout_iter.next_run() is False
        assert layout_iter.next_char() is False
        assert layout_iter.next_cluster() is False
        assert layout_iter.next_line() is False
        assert layout_iter.at_last_line() is True
        assert layout_iter.get_index() == 0
        # Even with no text in the layout, the layout will still have a
        # baseline corresponding to the selected font description.
        assert layout_iter.get_baseline() > 0

        assert isinstance(layout_iter.get_char_extents(), Rectangle)

        cluster_ink, cluster_logical = layout_iter.get_cluster_extents()
        assert isinstance(cluster_ink, Rectangle)
        assert isinstance(cluster_logical, Rectangle)

        run_ink, run_logical = layout_iter.get_run_extents()
        assert isinstance(run_ink, Rectangle)
        assert isinstance(run_logical, Rectangle)

        y0, y1 = layout_iter.get_line_yrange()
        assert y0 == 0
        # Even with no text in the layout, the layout will still have a
        # y-range corresponding to the selected font description.
        assert y1 > 0

        line_ink, line_logical = layout_iter.get_line_extents()
        assert isinstance(line_ink, Rectangle)
        assert isinstance(line_logical, Rectangle)

        layout_ink, layout_logical = layout_iter.get_layout_extents()
        assert isinstance(layout_ink, Rectangle)
        assert isinstance(layout_logical, Rectangle)

    def test_layout_iterator_run_returns_none(self):
        layout = Layout(self.pango_context)
        layout_iter = layout.get_iter()

        assert layout_iter.get_run() is None
