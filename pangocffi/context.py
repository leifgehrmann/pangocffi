from . import pango, gobject, ffi, FontDescription
import ctypes


class Context(object):

    def __init__(self):
        self._init_pointer(pango.pango_context_new())

    def _init_pointer(self, pointer: ctypes.c_void_p):
        self._pointer = ffi.gc(pointer, gobject.g_object_unref)

    def get_pointer(self) -> ctypes.c_void_p:
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ctypes.c_void_p) -> 'Context':
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    def __eq__(self, other):
        if isinstance(other, Context):
            return self.get_pointer() == other.get_pointer()
        return NotImplemented

    def set_font_description(self, desc: FontDescription) -> None:
        pango.pango_context_set_font_description(
            self._pointer, desc.get_pointer()
        )

    def get_font_description(self) -> FontDescription:
        return FontDescription.from_pointer(
            pango.pango_context_get_font_description(self._pointer)
        )
