from . import (
    FontDescription,
    Stretch,
    Style,
    Underline,
    Variant,
    Weight,
    ffi,
    gobject,
    pango,
)


class Attribute:
    """
    The :class:`Attributes` — Font and other attributes for annotating text
    """

    def _init_pointer(self, pointer: ffi.CData):
        self._pointer = ffi.gc(pointer, pango.pango_attribute_destroy)

    @classmethod
    def from_pointer(cls, pointer: ffi.CData) -> "Attribute":
        """
        Instantiates a :class:`Attribute` from a pointer.

        :return:
            the Attribute.
        """
        if pointer == ffi.NULL:
            raise ValueError("Null pointer")
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    def get_pointer(self) -> ffi.CData:
        """
        Returns the pointer to the context

        :return:
            the pointer to the context.
        """
        return self._pointer

    def __eq__(self, other: "Attribute") -> bool:
        if isinstance(other, Attribute):
            return bool(
                pango.pango_attribute_equal(self.get_pointer(), other.get_pointer())
            )
        return NotImplemented

    @property
    def start_index(self):
        return self._start_index

    @start_index.setter
    def start_index(self, start_index: int):
        """
        Set's the Start Index of a Attribute.

        :param start_index:
            the start index of the range. Should be >=0.
        """
        assert start_index >= 0
        self._start_index = start_index
        start = ffi.cast("guint", start_index)
        self._pointer.start_index = start

    @property
    def end_index(self):
        return self._end_index

    @end_index.setter
    def end_index(self, end_index: int):
        """
        Set's the End Index of a Attribute.

        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        assert end_index >= 0
        self._start_index = end_index
        end = ffi.cast("guint", end_index)
        self._pointer.start_index = end

    @classmethod
    def from_language(
        cls, language, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        API not implemented
        """
        temp = cls.from_pointer(pango.pango_attr_language_new(language))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_family(
        cls, family: str, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font family attribute.

        :param family:
            the font family
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_family_new(family))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_style(
        cls, style: Style, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font slant style attribute.

        :param style:
            the slant style
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_style_new(style.value))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_variant(
        cls, variant: Variant, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font variant attribute (normal or small caps)

        :param variant:
            the variant
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_variant_new(variant.value))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_stretch(
        cls, stretch: Stretch, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font stretch attribute

        :param stretch:
            the stretch
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_stretch_new(stretch.value))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_weight(
        cls, weight: Weight, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font weight attribute.

        :param weight:
            the weight
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_weight_new(weight.value))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_size(
        cls, size: int, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font-size attribute in fractional points.

        :param size:
            the font size, in PANGO_SCALEths of a point.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_size_new(size))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_size_absolute(
        cls, absolute_size: int, start_index: int = 0, end_index: int = 1
    ):
        """
        Create a new font-size attribute in device units.

        :param size:
            the font size, in PANGO_SCALEths of a device unit.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_size_new_absolute(size))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_font_desc(
        cls, font_desc: FontDescription, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new font description attribute. This attribute allows setting family, style, weight, variant, stretch, and size simultaneously.

        :param font_desc:
            the font description
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_font_desc_new(font_desc._pointer))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_foreground_color(
        cls,
        red: int,
        green: int,
        blue: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new foreground color attribute.

        :param red:
            the red value (ranging from 0 to 65535)
        :param green:
            the green value (ranging from 0 to 65535)
        :param blue:
            the blue value (ranging from 0 to 65535)
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(pango.pango_attr_foreground_new(red, green, blue))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_background_color(
        cls,
        red: int,
        green: int,
        blue: int,
        start_index: int = 0,
        end_index: int = 1,
    ):
        """
        Create a new background color attribute.

        :param red:
            the red value (ranging from 0 to 65535)
        :param green:
            the green value (ranging from 0 to 65535)
        :param blue:
            the blue value (ranging from 0 to 65535)
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(pango.pango_attr_background_new(red, green, blue))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_strikethrough(
        cls, strikethrough: bool, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new strike-through attribute.

        :param strikethrough:
            True if the text should be struck-through.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        strikethrough = ffi.cast("gboolean", strikethrough)
        temp = cls.from_pointer(pango.pango_attr_strikethrough_new(strikethrough))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_strikethrough_color(
        cls,
        red: int,
        green: int,
        blue: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new strikethrough color attribute. This attribute modifies the color of strikethrough lines.
        If not set, strikethrough lines will use the foreground color.

        :param red:
            the red value (ranging from 0 to 65535)
        :param green:
            the green value (ranging from 0 to 65535)
        :param blue:
            the blue value (ranging from 0 to 65535)
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(
            pango.pango_attr_strikethrough_color_new(red, green, blue)
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_underline(
        cls, underline: Underline, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new underline-style attribute.

        :param underline:
            the underline style.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        temp = cls.from_pointer(pango.pango_attr_underline_new(underline))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_underline_color(
        cls, red: int, green: int, blue: int, start_index: int = 0, end_index: int = 1
    ) -> "Attribute":
        """
        Create a new underline color attribute. This attribute modifies the color of underlines.
        If not set, underlines will use the foreground color.

        :param red:
            the red value (ranging from 0 to 65535)
        :param green:
            the green value (ranging from 0 to 65535)
        :param blue:
            the blue value (ranging from 0 to 65535)
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(pango.pango_attr_underline_color_new(red, green, blue))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp


class Language:
    def __init__(self) -> None:
        pass
