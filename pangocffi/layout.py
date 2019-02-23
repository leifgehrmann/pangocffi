from . import pango, gobject, ffi, Context, Alignment, Rectangle, FontDescription
import ctypes
from typing import Tuple, Optional


class Layout(object):

    def __init__(self, context: Context):
        self._init_pointer(pango.pango_layout_new(context.get_pointer()))

    def _init_pointer(self, pointer: ctypes.c_void_p):
        self._pointer = ffi.gc(pointer, gobject.g_object_unref)

    @classmethod
    def from_pointer(cls, pointer: ctypes.c_void_p) -> 'Layout':
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    def get_pointer(self) -> ctypes.c_void_p:
        return self._pointer

    def get_context(self) -> Context:
        return Context.from_pointer(pango.pango_layout_get_context(self._pointer))

    def set_text(self, text):
        text_pointer = ffi.new('char[]', text.encode('utf8'))
        pango.pango_layout_set_text(self._pointer, text_pointer, -1)

    def set_markup(self, markup: str) -> None:
        markup_pointer = ffi.new('char[]', markup.encode('utf8'))
        pango.pango_layout_set_markup(self._pointer, markup_pointer, -1)

    def set_font_description(self, desc: FontDescription) -> None:
        pango.pango_layout_set_font_description(self._pointer, desc.get_pointer())

    def get_font_description(self) -> Optional[FontDescription]:
        desc_pointer = pango.pango_layout_get_font_description(self._pointer)
        if desc_pointer == ffi.NULL:
            return None
        return FontDescription.from_pointer(desc_pointer)

    def set_width(self, width: int) -> None:
        pango.pango_layout_set_width(self._pointer, width)

    def get_width(self) -> int:
        return pango.pango_layout_get_width(self._pointer)

    def set_height(self, height: int) -> None:
        pango.pango_layout_set_height(self._pointer, height)

    def get_height(self) -> int:
        return pango.pango_layout_get_height(self._pointer)

    def set_alignment(self, alignment: Alignment) -> None:
        pango.pango_layout_set_alignment(self._pointer, alignment.value)

    def get_alignment(self) -> Alignment:
        return Alignment(pango.pango_layout_get_alignment(self._pointer))

    def get_extents(self) -> Tuple[Rectangle, Rectangle]:
        ink_rect_pointer = ffi.new("PangoRectangle *")
        logical_rect_pointer = ffi.new("PangoRectangle *")
        pango.pango_layout_get_extents(self._pointer, ink_rect_pointer, logical_rect_pointer)
        return Rectangle.from_pointer(ink_rect_pointer), Rectangle.from_pointer(logical_rect_pointer)

    def get_size(self) -> Tuple[int, int]:
        width_pointer = ffi.new("int *")
        height_pointer = ffi.new("int *")
        pango.pango_layout_get_size(self._pointer, width_pointer, height_pointer)
        return width_pointer[0], height_pointer[0]
