import ctypes
from dataclasses import dataclass


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int

    @staticmethod
    def from_pointer(pointer: ctypes.c_void_p) -> 'Rectangle':
        return Rectangle(
            x=pointer.x,
            y=pointer.y,
            width=pointer.width,
            height=pointer.height
        )
