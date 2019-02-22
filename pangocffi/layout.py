from . import pango, gobject, ffi, Context, Alignment
import ctypes


class Layout(object):

    def __init__(self, context: Context):
        self._pointer = ffi.gc(pango.pango_layout_new(context.get_pointer()), gobject.g_object_unref)

    def get_pointer(self) -> ctypes.c_void_p:
        return self._pointer

    def get_context(self) -> Context:
        return Context.from_pointer(pango.pango_layout_get_context(self._pointer))

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
