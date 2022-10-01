from typing import Optional
from . import ffi, PangoObject


class Rectangle(PangoObject):
    """
    The :class:`Rectangle` structure represents a rectangle. It is
    frequently used to represent the logical or ink extents of a single glyph
    or section of text.
    """

    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoRectangle"

    def __init__(
            self,
            pointer: Optional[ffi.CData] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None
    ):
        super().__init__(pointer)

        if width is not None:
            self.pointer.width = width
        if height is not None:
            self.pointer.height = height
        if x is not None:
            self.pointer.x = x
        if y is not None:
            self.pointer.y = y

    def _get_x(self) -> int:
        return self._pointer.x

    def _set_x(self, value: int):
        self._pointer.x = value

    x: int = property(_get_x, _set_x)
    """X coordinate of the left side of the rectangle."""

    def _get_y(self) -> int:
        return self._pointer.y

    def _set_y(self, value: int):
        self._pointer.y = value

    y: int = property(_get_y, _set_y)
    """Y coordinate of the the top side of the rectangle."""

    def _get_width(self) -> int:
        return self._pointer.width

    def _set_width(self, value: int):
        self._pointer.width = value

    width: int = property(_get_width, _set_width)
    """The width of the rectangle."""

    def _get_height(self) -> int:
        return self._pointer.height

    def _set_height(self, value: int):
        self._pointer.height = value

    height: int = property(_get_height, _set_height)
    """The height of the rectangle."""
