from typing import Optional
from . import ffi


class Rectangle:
    """
    The :class:`Rectangle` structure represents a rectangle. It is
    frequently used to represent the logical or ink extents of a single glyph
    or section of text.
    """
    def __init__(
            self,
            pointer: Optional[ffi.CData] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None
    ):
        if pointer is None:
            self.pointer = ffi.new("PangoRectangle *")
        else:
            self.pointer = pointer

        if width is not None:
            self.pointer.width = width
        if height is not None:
            self.pointer.height = height
        if x is not None:
            self.pointer.x = x
        if y is not None:
            self.pointer.y = y

    def get_pointer(self) -> ffi.CData:
        """
        Returns a pointer to the :class:`Rectangle`.

        :return:
            a pointer to ``PangoRectangle``
        """
        return self.pointer

    @staticmethod
    def from_pointer(pointer: ffi.CData) -> 'Rectangle':
        """
        Returns an instance of a :class:`Rectangle` from a pointer.

        :return:
            the :class:`Rectangle`.
        """
        return Rectangle(
            pointer=pointer
        )

    @property
    def x(self) -> int:
        """
        :return:
            X coordinate of the left side of the rectangle.
        :type: int
        """
        return self.pointer.x

    @x.setter
    def x(self, value: int):
        """
        :param value:
            Sets the X coordinate of the left side of the rectangle.
        """
        self.pointer.x = value

    @property
    def y(self) -> int:
        """
        :return:
            Y coordinate of the the top side of the rectangle.
        :type: int
        """
        return self.pointer.y

    @y.setter
    def y(self, value: int):
        """
        :param value:
            Sets the Y coordinate of the the top side of the rectangle.
        """
        self.pointer.y = value

    @property
    def width(self) -> int:
        """
        :return:
            width of the rectangle.
        :type: int
        """
        return self.pointer.width

    @width.setter
    def width(self, value: int):
        """
        :param value:
            Sets the width of the rectangle.
        """
        self.pointer.width = value

    @property
    def height(self) -> int:
        """
        :return:
            height of the rectangle.
        :type: int
        """
        return self.pointer.height

    @height.setter
    def height(self, value: int):
        """
        :param value:
            Sets the height of the rectangle.
        """
        self.pointer.height = value
