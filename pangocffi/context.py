from . import pango, gobject, ffi, FontDescription
import ctypes


class Context(object):
    """
    The :class:`Context` structure stores global information used to control
    the itemization process.
    """

    def __init__(self):
        """
        Creates a new PangoContext initialized to default values.

        This function is not particularly useful as it should always be
        followed by a :meth:`set_font_map()` call, and the function
        ``FontMap.create_context()`` does these two steps together and hence
        users are recommended to use that.

        If you are using Pango as part of a higher-level system, that system
        may have it's own way of create a :class:`Context`. For instance, the
        PangoCairo toolkit has pango_cairo_create_context(). Use those instead.
        """
        self._init_pointer(pango.pango_context_new())

    def _init_pointer(self, pointer: ctypes.c_void_p):
        self._pointer = ffi.gc(pointer, gobject.g_object_unref)

    def get_pointer(self) -> ctypes.c_void_p:
        """
        Returns the pointer to the context

        :return:
            the pointer to the context.
        """
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ctypes.c_void_p) -> 'Context':
        """
        Instantiates a :class:`Context` from a pointer.

        :return:
            the context.
        """
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
        """
        Set the default font description for the context.

        :param desc:
            the new pango font description.
        """
        pango.pango_context_set_font_description(
            self._pointer, desc.get_pointer()
        )

    def get_font_description(self) -> FontDescription:
        """
        Retrieve the default font description for the context.

        :return:
            the context's default font description.
        """
        return FontDescription.from_pointer(
            pango.pango_context_get_font_description(self._pointer)
        )
