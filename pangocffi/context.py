from . import pango, FontDescription, Gravity, GravityHint, PangoObject
from typing import Optional


class Context(PangoObject):
    """
    The :class:`Context` structure stores global information used to control
    the itemization process.
    """

    _INIT_METHOD = pango.pango_context_new

    def __init__(self):
        """
        Creates a new context initialized to default values.

        This function is not particularly useful as it should always be
        followed by a :meth:`set_font_map()` call: the function
        ``FontMap.create_context()`` does these two steps together and
        users are recommended to use that.

        If you are using Pango as part of a higher-level system, that system
        may have its own way of creating a :class:`Context`. For instance,
        PangoCairo has ``pango_cairo_create_context()``; use that instead.
        """
        super().__init__()

    def _get_font_description(self) -> FontDescription:
        return FontDescription.from_pointer(
            pango.pango_context_get_font_description(self._pointer)
        )

    def _set_font_description(self, desc: FontDescription):
        pango.pango_context_set_font_description(self._pointer, desc.pointer)

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
    The base gravity for the context, which is used for laying out vertical
    text.
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
