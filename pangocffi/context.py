from . import pango, gobject, ffi
import ctypes


class Context(object):

    def __init__(self):
        self._init_pointer(pango.pango_context_new())

    def _init_pointer(self, pointer: ctypes.c_void_p):
        self._pointer = ffi.gc(pointer, gobject.g_object_unref)

    def get_pointer(self) -> ctypes.c_void_p:
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ctypes.c_void_p):
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    def __eq__(self, other):
        if isinstance(other, Context):
            return self.get_pointer() == other.get_pointer()
        return NotImplemented
