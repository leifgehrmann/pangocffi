from . import FontDescription, Underline, ffi, pango
from .enums import Gravity, GravityHint, Stretch, Style, Variant, Weight
from .rectangle import Rectangle


class Attribute:
    """
    The :class:`Attributes` — Font and other attributes for annotating text.
    Attributed text is used in a number of places in Pango.
    It is used as the input to the itemization process and also
    when creating a PangoLayout. The data types and functions in
    this section are used to represent and manipulate sets of
    attributes applied to a portion of text.
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
                pango.pango_attribute_equal(
                    self.get_pointer(),
                    other.get_pointer(),
                )
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
            end index of the range. The character at this index
            is not included in the range.
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
            the start index of the range.
            Should be >=0.
        :param end_index:
            end index of the range. The character
            at this index is not included in the range.
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
            end index of the range. The character at
            this index is not included in the range.
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
            end index of the range. The character at
            this index is not included in the range.
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
            end index of the range. The character at this
            index is not included in the range.
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
            end index of the range. The character at this
            index is not included in the range.
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
            end index of the range. The character at this
            index is not included in the range.
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
            end index of the range. The character at this index
            is not included in the range.
        """
        temp = cls.from_pointer(
            pango.pango_attr_size_new_absolute(
                absolute_size,
            ),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_font_desc(
        cls,
        font_desc: FontDescription,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new font description attribute. This attribute
        allows setting family, style, weight, variant,
        stretch, and size simultaneously.

        :param font_desc:
            the font description
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this index
            is not included in the range.
        """
        temp = cls.from_pointer(
            pango.pango_attr_font_desc_new(
                font_desc._pointer,
            )
        )
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
            end index of the range. The character at this
            index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(
            pango.pango_attr_foreground_new(
                red,
                green,
                blue,
            ),
        )
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
            end index of the range. The character at this
            index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(
            pango.pango_attr_background_new(
                red,
                green,
                blue,
            ),
        )
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
            end index of the range. The character at this index
            is not included in the range.
        """
        strikethrough = ffi.cast("gboolean", strikethrough)
        temp = cls.from_pointer(
            pango.pango_attr_strikethrough_new(
                strikethrough,
            ),
        )
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
        Create a new strikethrough color attribute. This attribute
        modifies the color of strikethrough lines.
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
            end index of the range. The character at this
            index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(
            pango.pango_attr_strikethrough_color_new(
                red,
                green,
                blue,
            )
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_underline(
        cls,
        underline: Underline,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new underline-style attribute.

        :param underline:
            the underline style.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        temp = cls.from_pointer(
            pango.pango_attr_underline_new(
                underline,
            ),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_underline_color(
        cls,
        red: int,
        green: int,
        blue: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new underline color attribute.
        This attribute modifies the color of underlines.
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
            end index of the range. The character at this
            index is not included in the range.
        """
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls.from_pointer(
            pango.pango_attr_underline_color_new(
                red,
                green,
                blue,
            ),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_shape(
        cls,
        ink_rect: Rectangle,
        logical_rectangle: Rectangle,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new shape attribute. A shape is used to impose
        a particular ink and logical rectangle on the result of
        shaping a particular glyph. This might be used, for
        instance, for embedding a picture or a widget inside a
        PangoLayout.

        :param ink_rect:
            ink rectangle to assign to each character
        :param logical_rectangle:
            logical rectangle to assign to each character
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        temp = cls.from_pointer(
            pango.pango_attr_shape_new(
                ink_rect.get_pointer(), logical_rectangle.get_pointer()
            ),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    # TODO: pango_attr_shape_new_with_data with data?
    @classmethod
    def from_scale(
        cls,
        scale_factor: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new font size scale attribute.
        The base font for the affected text will
        have its size multiplied by ``scale_factor``.

        :param scale_factor:
            factor to scale the font
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        scale_factor = ffi.cast("double", scale_factor)
        temp = cls.from_pointer(
            pango.pango_attr_scale_new(scale_factor),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_rise(
        cls,
        rise: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new baseline displacement attribute.

        :param rise:
            the amount that the text should be displaced vertically,
            in Pango units. Positive values displace the text
            upwards.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        rise = ffi.cast("int", rise)
        temp = cls.from_pointer(
            pango.pango_attr_rise_new(rise),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_letter_spacing_new(
        cls,
        letter_spacing: str,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new letter-spacing attribute.

        :param letter_spacing:
            amount of extra space to add between graphemes
            of the text, in Pango units.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        letter_spacing = ffi.cast("int", letter_spacing)
        temp = cls.from_pointer(
            pango.pango_attr_letter_spacing_new(letter_spacing),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_fallback(
        cls,
        enable_fallback: bool,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new font fallback attribute.

        If fallback is disabled, characters will only be used
        from the closest matching font on the system.
        No fallback will be done to other fonts on the system
        that might contain the characters in the text.

        :param enable_fallback:
            True if we should fall back on other fonts for
            characters the active font is missing.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        enable_fallback = ffi.cast("gboolean", enable_fallback)
        temp = cls.from_pointer(
            pango.pango_attr_fallback_new(enable_fallback),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_gravity(
        cls,
        gravity: Gravity,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new gravity attribute.

        :param gravity:
            the gravity value; should not be :class:`PANGO_GRAVITY_AUTO`.
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        temp = cls.from_pointer(
            pango.pango_attr_gravity_new(gravity.value()),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_gravity_hints(
        cls,
        hint: GravityHint,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new gravity hint attribute.

        :param hint:
            the gravity hint value from :class:`GravityHint`
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        temp = cls.from_pointer(
            pango.pango_attr_gravity_hint_new(hint.value()),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_font_features(
        cls,
        features: str,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new font features tag attribute.

        :param features:
            a string with OpenType font features, in CSS syntax
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        features = ffi.new("char[]", features.encode("utf8"))
        temp = cls.from_pointer(
            pango.pango_attr_font_features_new(features),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_foreground_alpha(
        cls,
        alpha: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new foreground alpha attribute.

        :param alpha:
            the alpha value, between 1 and 65536
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        alpha = ffi.cast("guint16", alpha)
        temp = cls.from_pointer(
            pango.pango_attr_foreground_alpha_new(alpha),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_background_alpha(
        cls,
        alpha: int,
        start_index: int = 0,
        end_index: int = 1,
    ) -> "Attribute":
        """
        Create a new background alpha attribute.

        :param alpha:
            the alpha value, between 1 and 65536
        :param start_index:
            the start index of the range. Should be >=0.
        :param end_index:
            end index of the range. The character at this
            index is not included in the range.
        """
        alpha = ffi.cast("guint16", alpha)
        temp = cls.from_pointer(
            pango.pango_attr_background_alpha_new(alpha),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp


class Language:
    def __init__(self) -> None:
        pass
