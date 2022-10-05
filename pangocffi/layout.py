from . import pango, gobject, ffi, PangoObject
from . import Context, FontDescription, AttrList
from . import Alignment, Rectangle, EllipsizeMode, WrapMode
from pangocffi import LayoutIter
from typing import Tuple, Optional


class Layout(PangoObject):
    """
    A Pango :class:`Layout` represents an entire paragraph of text. It is
    initialized with a Pango :class:`Context`, UTF-8 string and set of
    attributes for that string. Once that is done, the set of formatted lines
    can be extracted from the object, the layout can be rendered, and
    conversion between logical character positions within the layout's text,
    and the physical position of the resulting glyphs can be made.
    """

    _INIT_METHOD = pango.pango_layout_new
    _GC_METHOD = gobject.g_object_unref

    def __init__(self, context: Context):
        return super().__init__(None, context.pointer)

    @property
    def context(self) -> Context:
        """The :class:`Context` used for this layout."""
        return Context.from_pointer(
            pango.pango_layout_get_context(self._pointer),
        )

    def _get_text(self) -> str:
        text_pointer = pango.pango_layout_get_text(self._pointer)
        return ffi.string(text_pointer).decode("utf-8")

    def _set_text(self, text: str) -> None:
        text_pointer = ffi.new("char[]", text.encode("utf8"))
        pango.pango_layout_set_text(self._pointer, text_pointer, -1)

    text: str = property(_get_text, _set_text)
    """
    The text contained in the layout.

    Note that if you have used :meth:`apply_markup()` on the layout before,
    you may want to clear the :attr:`attributes` from the markup when setting
    this property, as attributes are not cleared automatically.
    """

    def _get_font_description(self) -> Optional[FontDescription]:
        desc_pointer = pango.pango_layout_get_font_description(self._pointer)
        if desc_pointer == ffi.NULL:
            return None
        return FontDescription.from_pointer(desc_pointer)

    def _set_font_description(self, desc: Optional[FontDescription]) -> None:
        value = desc.pointer if isinstance(desc, FontDescription) else ffi.NULL
        pango.pango_layout_set_font_description(self._pointer, value)

    font_description: Optional[FontDescription] = property(
        _get_font_description, _set_font_description
    )
    """
    The default font description for the layout. If no font
    description is set, the font description from the layout's context is used.
    """

    def _get_width(self) -> int:
        return pango.pango_layout_get_width(self._pointer)

    def _set_width(self, width: int) -> None:
        pango.pango_layout_set_width(self._pointer, width)

    width: int = property(_get_width, _set_width)
    """The width to which the lines of the layout should wrap or ellipsize."""

    def _get_height(self) -> int:
        return pango.pango_layout_get_height(self._pointer)

    def _set_height(self, height: int) -> None:
        pango.pango_layout_set_height(self._pointer, height)

    height: int = property(_get_height, _set_height)
    """
    The height to which the layout should be ellipsized at.

    If the height is positive, it will be the maximum height of the layout.
    Only lines which fit will be shown, and any omitted text is replaced
    by an ellipsis. At least one line is included in each paragraph
    regardless of how small the height value is; a value of zero will
    render exactly one line for the entire layout.

    If height is negative, it will be the (negative of) maximum number of
    lines per paragraph. That is, the total number of lines shown may well
    be more than this value if the layout contains multiple paragraphs of
    text. The default value of -1 means that first line of each paragraph
    is ellipsized.

    This property only has effect if a positive width is set on layout and
    its ellipsization mode is not ``NONE``. The behavior is undefined if a
    height other than -1 is set and ellipsization mode is set to ``NONE``.
    """

    def _get_spacing(self) -> int:
        return pango.pango_layout_get_spacing(self._pointer)

    def _set_spacing(self, spacing: int) -> None:
        pango.pango_layout_set_spacing(self._pointer, spacing)

    spacing: int = property(_get_spacing, _set_spacing)
    """
    The amount of spacing, in Pango units, between the lines of the layout.
    """

    def _get_alignment(self) -> Alignment:
        return Alignment(pango.pango_layout_get_alignment(self._pointer))

    def _set_alignment(self, alignment: Alignment) -> None:
        pango.pango_layout_set_alignment(self._pointer, alignment.value)

    alignment: Alignment = property(_get_alignment, _set_alignment)
    """
    The alignment of the layout: how partial lines are positioned
    within the horizontal space available.
    """

    def _get_ellipsize(self) -> EllipsizeMode:
        return EllipsizeMode(pango.pango_layout_get_ellipsize(self._pointer))

    def _set_ellipsize(self, ellipsize: EllipsizeMode) -> None:
        pango.pango_layout_set_ellipsize(self._pointer, ellipsize.value)

    ellipsize: EllipsizeMode = property(_get_ellipsize, _set_ellipsize)
    """The ellipsize mode of the layout."""

    def _get_wrap(self) -> WrapMode:
        return WrapMode(pango.pango_layout_get_wrap(self._pointer))

    def _set_wrap(self, wrap: WrapMode) -> None:
        pango.pango_layout_set_wrap(self._pointer, wrap.value)

    wrap: WrapMode = property(_get_wrap, _set_wrap)
    """The wrap mode of the layout."""

    def _get_attributes(self) -> Optional[AttrList]:
        attrs_pointer = pango.pango_layout_get_attributes(self._pointer)
        if attrs_pointer == ffi.NULL:
            return None
        return AttrList.from_pointer(attrs_pointer)

    def _set_attributes(self, attrs: Optional[AttrList]) -> None:
        if attrs is None:
            pango.pango_layout_set_attributes(self._pointer, ffi.NULL)
        else:
            pango.pango_layout_set_attributes(
                self._pointer,
                attrs.pointer
            )

    def _del_attributes(self) -> None:
        self._set_attributes(None)

    attributes = property(_get_attributes, _set_attributes, _del_attributes)
    """
    The text attributes for this layout.

    :param attrs: a :class:`AttrList`
    """

    def apply_markup(self, markup: str) -> None:
        """
        Sets the layout text and attribute list from marked-up text.

        :param markup:
            marked-up text
        """
        markup_pointer = ffi.new("char[]", markup.encode("utf8"))
        pango.pango_layout_set_markup(self._pointer, markup_pointer, -1)

    def get_extents(self) -> Tuple[Rectangle, Rectangle]:
        """
        Computes the logical and ink extents of the layout.
        Logical extents are usually what you want for positioning things.
        Note that both extents may have non-zero x and y.
        You may want to use those to offset where you render the layout.
        Not doing that is a very typical bug that shows up as right-to-left
        layouts not being correctly positioned in a layout with a set width.

        The extents are given in layout coordinates and in Pango units;
        layout coordinates begin at the top left corner of the layout.

        :return:
            a tuple containing two :class:`Rectangle` objects.
            The first is the extent of the layout as drawn.
            The second is the logical extent of the layout.
        """
        ink_rect = Rectangle()
        logical_rect = Rectangle()
        pango.pango_layout_get_extents(
            self._pointer, ink_rect.pointer, logical_rect.pointer
        )
        return ink_rect, logical_rect

    def get_size(self) -> Tuple[int, int]:
        """
        Determines the logical width and height of the layout in Pango units.
        This is simply a convenience function around :meth:`get_extents()`.

        :return:
            a tuple containing the logical width and height, respectively.
        """
        width_pointer = ffi.new("int *")
        height_pointer = ffi.new("int *")
        pango.pango_layout_get_size(
            self._pointer,
            width_pointer,
            height_pointer,
        )
        width = width_pointer[0]
        height = height_pointer[0]
        return width, height

    def get_baseline(self) -> int:
        """
        Returns the Y coordinate of the first line's baseline in the layout.

        :return:
            baseline of the :class:`Layout`'s first, line from the top
        """
        return pango.pango_layout_get_baseline(self._pointer)

    def get_line_count(self) -> int:
        """
        Returns the number of lines.

        :return:
            the line count
        """
        return pango.pango_layout_get_line_count(self._pointer)

    def get_iter(self) -> LayoutIter:
        """
        Returns an iterator to iterate over the visual extents of the layout.

        :return:
            the layout iterator
        """
        layout_iterator_pointer = pango.pango_layout_get_iter(self._pointer)
        return LayoutIter(layout_iterator_pointer)
