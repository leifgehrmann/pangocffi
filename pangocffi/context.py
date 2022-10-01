from . import pango, gobject, ffi, FontDescription, Gravity, GravityHint
from typing import Optional

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
        may have its own way of creating a :class:`Context`. For instance,
        PangoCairo has ``pango_cairo_create_context()``; use that instead.
        """
        self._init_pointer(pango.pango_context_new(), gc=True)

    def _init_pointer(self, pointer: ffi.CData, gc: bool):
        if gc:
            self._pointer = ffi.gc(pointer, gobject.g_object_unref)
        else:
            self._pointer = pointer

    def _get_pointer(self) -> ffi.CData:
        return self._pointer

    pointer: ffi.CData = property(_get_pointer)
    """The C pointer to the context."""

    @classmethod
    def from_pointer(cls, pointer: ffi.CData, gc: bool = False) -> 'Context':
        """
        Instantiates a :class:`Context` from a pointer.

        :param pointer:
            a pointer to a Pango Context.
        :param gc:
            whether to garbage collect the pointer. Defaults to ``False``.
        :return:
            the context.
        """
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer, gc)
        return self

    def __eq__(self, other):
        if isinstance(other, Context):
            return self.pointer == other.pointer
        return NotImplemented

    def _get_font_description(self) -> FontDescription:
        return FontDescription.from_pointer(
            pango.pango_context_get_font_description(self._pointer)
        )

    def _set_font_description(self, desc: FontDescription):
        pango.pango_context_set_font_description(
            self._pointer, desc.get_pointer()
        )

    font_description: Optional[FontDescription] = property(
        _get_font_description, _set_font_description
    )
    """
    The default font description for the context.

    :param desc:
        the new Pango font description.
    """

    def _get_base_gravity(self) -> Gravity:
        return Gravity(pango.pango_context_get_base_gravity(self._pointer))

    def _set_base_gravity(self, gravity: Gravity):
        pango.pango_context_set_base_gravity(self._pointer, gravity.value)

    base_gravity: Gravity = property(_get_base_gravity, _set_base_gravity)
    """
    The base gravity for the context, which is used for laying out vertical text.
    """

    def _get_gravity(self) -> Gravity:
        return Gravity(pango.pango_context_get_gravity(self._pointer))

    gravity: Gravity = property(_get_gravity)
    """
    The gravity for the context. This is similar to :attr:`base_gravity`,
    unless it's :meth:`Gravity.AUTO`; :meth:`get_for_matrix()` is used to
    retrieve the appropriate gravity from the current context matrix.
    """

    def _get_gravity_hint(self) -> GravityHint:
        return GravityHint(pango.pango_context_get_gravity_hint(self._pointer))

    def _set_gravity_hint(self, hint: GravityHint):
        pango.pango_context_set_gravity_hint(self._pointer, hint.value)

    gravity_hint: GravityHint = property(_get_gravity_hint, _set_gravity_hint)
    """
    The gravity hint for the context, which is used when laying out vertical
    text, and is only relevant if the gravity of the context is
    :meth:`Gravity.EAST` or :meth:`Gravity.WEST`.
    """
