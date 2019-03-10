from typing import Tuple
from . import pango, ffi
from . import Layout, Rectangle


class LayoutIterator:
    """
    A LayoutIterator can be used to iterate over the visual extents of a
    Pango :class:`Layout`.
    """

    def __init__(self, layout: Layout):
        """
        Returns an iterator to iterate over the visual extents of the layout.

        :param layout:
            a Pango :class:`Layout`
        """
        self._init_pointer(pango.pango_layout_get_iter(layout.get_pointer()))

    def _init_pointer(self, pointer: ffi.CData):
        self._pointer = ffi.gc(pointer, pango.pango_layout_iter_free)

    def get_pointer(self) -> ffi.CData:
        """
        Returns the pointer to this iterator.

        :return:
            a pointer to the iterator.
        """
        return self._pointer

    def next_run(self) -> bool:
        """
        Moves the iterator forward to the next run in visual order. If the
        iterator was already at the end of the layout, it will
        return ``False``.

        :return:
            whether motion was possible.
        """
        return bool(pango.pango_layout_iter_next_run(self._pointer))

    def next_char(self) -> bool:
        """
        Moves the iterator forward to the next character in visual order. If
        the iterator was already at the end of the layout, it will
        return ``False``.

        :return:
            whether motion was possible.
        """
        return bool(pango.pango_layout_iter_next_char(self._pointer))

    def next_cluster(self) -> bool:
        """
        Moves the iterator forward to the next cluster in visual order. If
        the iterator was already at the end of the layout, it will
        return ``False``.

        :return:
            whether motion was possible.
        """
        return bool(pango.pango_layout_iter_next_cluster(self._pointer))

    def next_line(self) -> bool:
        """
        Moves the iterator forward to the start of the next line. If
        the iterator was already at the end of the layout, it will
        return ``False``.

        :return:
            whether motion was possible.
        """
        return bool(pango.pango_layout_iter_next_line(self._pointer))

    def at_last_line(self) -> bool:
        """
        Determines whether the iterator is on the last line of the layout.

        :return:
            ``True`` if iterator is on the last line.
        """
        return bool(pango.pango_layout_iter_at_last_line(self._pointer))

    def get_index(self) -> int:
        """
        Returns the current byte index. Note that iterating forward by char
        moves in visual order, not logical order, so indexes may not be
        sequential. Also, the index may be equal to the length of the text
        in the layout, if on the NULL run (see :meth:`get_run()`).

        :return:
            The current byte index.
        """
        return pango.pango_layout_iter_get_index(self._pointer)

    def get_baseline(self) -> int:
        """
        Returns the Y position of the current line's baseline, in layout
        coordinates (origin at top left of the entire layout).

        :return:
            The baseline of the current line.
        """
        return pango.pango_layout_iter_get_baseline(self._pointer)

    # def get_run(_readonly)

    # def get_line(_readonly)

    # def get_layout

    def get_char_extents(self) -> Rectangle:
        """
        Returns the extents of the current character, in layout coordinates
        (origin is the top left of the entire layout). Only logical extents
        can sensibly be obtained for characters; ink extents make sense only
        down to the level of clusters.

        :return:
             a rectangle representing the logical extent of a character.
        """
        logical_rect = Rectangle()
        pango.pango_layout_iter_get_char_extents(
            self._pointer,
            logical_rect.get_pointer()
        )
        return logical_rect

    def get_cluster_extents(self) -> Tuple[Rectangle, Rectangle]:
        """
        Returns the extents of the current cluster, in layout coordinates (origin
        is the top left of the entire layout).

        :return:
            a tuple containing two :class:`Rectangle` objects.
            The first is the extent of the cluster as drawn.
            The second is the logical extent.
        """
        ink_rect = Rectangle()
        logical_rect = Rectangle()
        pango.pango_layout_iter_get_cluster_extents(
            self._pointer,
            ink_rect.get_pointer(),
            logical_rect.get_pointer()
        )
        return ink_rect, logical_rect

    def get_run_extents(self) -> Tuple[Rectangle, Rectangle]:
        """
        Returns the extents of the current run, in layout coordinates (origin
        is the top left of the entire layout).

        :return:
            a tuple containing two :class:`Rectangle` objects.
            The first is the extent of the run as drawn.
            The second is the logical extent.
        """
        ink_rect = Rectangle()
        logical_rect = Rectangle()
        pango.pango_layout_iter_get_run_extents(
            self._pointer,
            ink_rect.get_pointer(),
            logical_rect.get_pointer()
        )
        return ink_rect, logical_rect

    def get_line_yrange(self) -> Tuple[int, int]:
        """
        Divides the vertical space in the :class:`Layout` being iterated over
        between the lines in the layout, and returns the space belonging to
        the current line. A line's range includes the line's logical
        extents, plus half of the spacing above and below the line, if
        :meth:`Layout.set_spacing()` has been called to set layout spacing.
        The Y positions are in layout coordinates (origin at top left of
        the entire layout).

        :return:
            a tuple containing two integers.
            The first is the y position of the start of the line.
            The second is the y position of the end of the line
        """
        y0_pointer = ffi.new("int *")
        y1_pointer = ffi.new("int *")
        pango.pango_layout_iter_get_line_yrange(
            self._pointer,
            y0_pointer,
            y1_pointer
        )
        y0 = y0_pointer[0]
        y1 = y1_pointer[0]
        return y0, y1

    def get_layout_extents(self) -> Tuple[Rectangle, Rectangle]:
        """
        Returns the extents of the :class:`Layout` being iterated over.

        :return:
            a tuple containing two :class:`Rectangle` objects.
            The first is the extent of the run as drawn.
            The second is the logical extent.
        """
        ink_rect = Rectangle()
        logical_rect = Rectangle()
        pango.pango_layout_iter_get_run_extents(
            self._pointer,
            ink_rect.get_pointer(),
            logical_rect.get_pointer()
        )
        return ink_rect, logical_rect
