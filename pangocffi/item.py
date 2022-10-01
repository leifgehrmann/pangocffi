from . import pango, PangoObject


class Item(PangoObject):
    """
    The :class:`Item` structure stores information about a segment of text.
    """

    _GC_METHOD = pango.pango_item_free
    _COPY_METHOD = pango.pango_item_copy

    @property
    def offset(self) -> int:
        """Byte offset of the start of this item in text."""
        return self._pointer.offset

    @property
    def length(self) -> int:
        """Length of this item in bytes."""
        return self._pointer.length

    @property
    def num_chars(self) -> int:
        """Length of this item in characters."""
        return self._pointer.num_chars
