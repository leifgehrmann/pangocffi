from . import pango, ffi, PangoObject, TabAlign
from typing import List, Tuple, Optional


class TabArray(PangoObject):

    _INIT_METHOD = pango.pango_tab_array_new
    _GC_METHOD = pango.pango_tab_array_free
    _COPY_METHOD = pango.pango_tab_array_copy

    def __init__(self):
        return super().__init__(None, 0, False)

    def __len__(self):
        return pango.pango_tab_array_get_size(self._pointer)

    def _get_tabs(self) -> List[Tuple[TabAlign, int]]:
        size = len(self)
        alignments = ffi.new("PangoTabAlign**")
        locations = ffi.new("gint**")
        pango.pango_tab_array_get_tabs(self._pointer, alignments, locations)
        if alignments[0] == ffi.NULL or locations[0] == ffi.NULL:
            return []
        else:
            return [(TabAlign(alignments[0][i]), locations[0][i])
                    for i in range(size)]

    def _set_tabs(self, tabs: List[Tuple[TabAlign, int]]) -> None:
        pango.pango_tab_array_resize(self._pointer, len(tabs))
        for i in range(len(tabs)):
            pango.pango_tab_array_set_tab(self._pointer, i, tabs[i][0].value,
                                          tabs[i][1])

    tabs: str = property(_get_tabs, _set_tabs)
    """
    Alignment and location of the tabs.
    """

    def _get_decimal_point(self) -> List[Optional[str]]:
        size = len(self)
        ret = []
        for i in range(size):
            decimal_point = pango.pango_tab_array_get_decimal_point(
                            self._pointer, i)
            if decimal_point == 0:
                ret.append(None)
            else:
                ret.append(chr(decimal_point))
        return ret

    def _set_decimal_point(self, decimal_point: List[Optional[str]]) -> None:
        if len(decimal_point) != len(self):
            raise IndexError()
        for i in range(len(decimal_point)):
            value = ord(decimal_point[i]) if decimal_point[i] is not None \
                                          else 0
            pango.pango_tab_array_set_decimal_point(self._pointer, i, value)

    decimal_point: str = property(_get_decimal_point, _set_decimal_point)
    """
    Unicode character to use as decimal point.

    This is only relevant for tabs with :attr:`TabAlign.DECIMAL`
    alignment, which align content at the first occurrence of the decimal
    point character.

    The default value of :const:`None` means that Pango will use the
    decimal point according to the current locale.

    :raises: :class:`IndexError` when trying to assign more or less
      elements than defined tab stops.
    """

    def _set_positions_in_pixels(self, positions_in_pixels: bool) -> None:
        pango.pango_tab_array_set_positions_in_pixels(self._pointer,
                                                      positions_in_pixels)

    def _get_positions_in_pixels(self) -> bool:
        return pango.pango_tab_array_get_positions_in_pixels(self._pointer) \
               != 0

    positions_in_pixels = property(_get_positions_in_pixels,
                                   _set_positions_in_pixels)
    """
    True if tab positions are in pixels.
    """
