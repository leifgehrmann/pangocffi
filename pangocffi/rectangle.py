import ctypes


class Rectangle:
    """
    The :class:`Rectangle` structure represents a rectangle. It is
    frequently used to represent the logical or ink extents of a single glyph
    or section of text.
    """
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @staticmethod
    def from_pointer(pointer: ctypes.c_void_p) -> 'Rectangle':
        """
        Returns an instance of a :class:`Rectangle` from a pointer.

        :return:
            the :class:`Rectangle`.
        """
        return Rectangle(
            x=pointer.x,
            y=pointer.y,
            width=pointer.width,
            height=pointer.height
        )
