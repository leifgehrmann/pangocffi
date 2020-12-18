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

    def __init__(self):
        self._pointer = None
        self._start_index = None
        self._end_index = None

    @classmethod
    def _init_pointer(cls, pointer: ffi.CData) -> "Attribute":
        self = object.__new__(cls)
        self._pointer = ffi.gc(pointer, pango.pango_attribute_destroy)
        return self

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
        self._pointer = pointer
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
        raise NotImplementedError

    @property
    def start_index(self):
        return self._start_index

    @start_index.setter
    def start_index(self, start_index: int):
        """
        Set's the Start Index of a Attribute.

        :param start_index:
            the start index of the range. Should be >=0.
        :raises: AssertionError
            When ``start_index`` isn't a :class:`int`.
        """
        assert isinstance(start_index, int), "start_index isn't a int"
        assert start_index >= pango.PANGO_ATTR_INDEX_FROM_TEXT_BEGINNING, \
            "start_index is too low"
        assert start_index < pango.PANGO_ATTR_INDEX_TO_TEXT_END, \
            "start_index is too high"
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
        :raises: AssertionError
            When ``end_index`` isn't a :class:`int`.
        """
        assert isinstance(end_index, int), "end_index isn't a int"
        assert end_index <= pango.PANGO_ATTR_INDEX_TO_TEXT_END, \
            "end_index is too high"
        self._end_index = end_index
        end = ffi.cast("guint", end_index)
        self._pointer.start_index = end

    # @classmethod
    # def from_language(
    #    cls, language, start_index: int = 0, end_index: int = 1
    # ) -> "Attribute":
    #    """
    #    API not implemented
    #    """
    #    temp = cls._init_pointer(pango.pango_attr_language_new(language))
    #    temp.start_index = start_index
    #    temp.end_index = end_index
    #    return temp

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
        :return:
            the Attribute.
        """
        family = ffi.new("char[]", family.encode("utf-8"))
        temp = cls._init_pointer(pango.pango_attr_family_new(family))
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``style`` isn't a :class:`Style`.
        """
        assert isinstance(style, Style), "style isn't a Style"
        temp = cls._init_pointer(pango.pango_attr_style_new(style.value))
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``variant`` isn't a :class:`Variant`.
        """
        assert isinstance(variant, Variant), "variant isn't a Variant"
        temp = cls._init_pointer(pango.pango_attr_variant_new(variant.value))
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``stretch`` isn't a :class:`Stretch`.
        """
        assert isinstance(stretch, Stretch), "stretch isn't a Stretch"
        temp = cls._init_pointer(pango.pango_attr_stretch_new(stretch.value))
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``weight`` isn't a :class:`Weight`.
        """
        assert isinstance(weight, Weight), "weight isn't a Weight"
        temp = cls._init_pointer(pango.pango_attr_weight_new(weight.value))
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``size`` isn't a :class:`int`.
        """
        assert isinstance(size, int), "size isn't int"
        size = ffi.cast("int", size)
        temp = cls._init_pointer(pango.pango_attr_size_new(size))
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_size_absolute(
        cls, size: int, start_index: int = 0, end_index: int = 1
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``absolute_size`` isn't a :class:`int`.
        """
        assert isinstance(size, int), "size isn't int"
        size = ffi.cast("int", size)
        temp = cls._init_pointer(
            pango.pango_attr_size_new_absolute(
                size,
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``font_desc`` isn't a :class:`FontDescription`.
        """
        assert isinstance(
            font_desc, FontDescription
        ), "font_desc isn't a FontDescription"
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``red`` or ``blue`` or ``green`` isn't a :class:`int`.
        """
        assert isinstance(red, int), "red isn't a int"
        assert isinstance(green, int), "green isn't a int"
        assert isinstance(blue, int), "blue isn't a int"
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``red`` or ``blue`` or ``green`` isn't a :class:`int`.
        """
        assert isinstance(red, int), "red isn't a int"
        assert isinstance(green, int), "green isn't a int"
        assert isinstance(blue, int), "blue isn't a int"
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``strikethrough`` isn't a :class:`bool`.
        """
        assert isinstance(strikethrough, int), "strikethrough isn't a bool"
        strikethrough = ffi.cast("gboolean", strikethrough)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``red`` or ``blue`` or ``green`` isn't a :class:`int`.
        """
        assert isinstance(red, int), "red isn't a int"
        assert isinstance(green, int), "green isn't a int"
        assert isinstance(blue, int), "blue isn't a int"
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``underline`` isn't a :class:`Underline`.
        """
        assert isinstance(underline, Underline), "underline isn't a Underline"
        temp = cls._init_pointer(
            pango.pango_attr_underline_new(
                underline.value,
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``red`` or ``blue`` or ``green`` isn't a :class:`int`.
        """
        assert isinstance(red, int), "red isn't a int"
        assert isinstance(green, int), "green isn't a int"
        assert isinstance(blue, int), "blue isn't a int"
        red = ffi.cast("guint16", red)
        green = ffi.cast("guint16", green)
        blue = ffi.cast("guint16", blue)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``ink_rect`` or ``logical_rectangle`` isn't a
            :class:`Rectangle`.
        """
        assert isinstance(ink_rect, Rectangle), "ink_rect isn't a Rectangle"
        assert isinstance(
            logical_rectangle, Rectangle
        ), "logical_rectangle isn't a Rectangle"
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``scale_factor`` isn't a :class:`int`.
        """
        assert isinstance(scale_factor, int), "scale_factor isn't a int"
        scale_factor = ffi.cast("double", scale_factor)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``rise`` isn't a :class:`int`.
        """
        assert isinstance(rise, int), "rise isn't a int"
        rise = ffi.cast("int", rise)
        temp = cls._init_pointer(
            pango.pango_attr_rise_new(rise),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    @classmethod
    def from_letter_spacing(
        cls,
        letter_spacing: int,
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``letter_spacing`` isn't a :class:`int`.
        """
        assert isinstance(letter_spacing, int), "rise isn't a int"
        letter_spacing = ffi.cast("int", letter_spacing)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``enable_fallback`` isn't a :class:`bool`.
        """
        assert isinstance(enable_fallback, bool),\
            "enable_fallback isn't a bool"
        enable_fallback = ffi.cast("gboolean", enable_fallback)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``gravity`` isn't a :class:`Gravity`.
        """
        assert isinstance(gravity, Gravity), "gravity isn't a Gravity"
        temp = cls._init_pointer(
            pango.pango_attr_gravity_new(gravity.value),
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``hint`` isn't a :class:`GravityHint`.
        """
        assert isinstance(hint, GravityHint), "hint isn't a GravityHint"
        temp = cls._init_pointer(
            pango.pango_attr_gravity_hint_new(hint.value),
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``features`` isn't a :class:`str`.
        """
        assert isinstance(features, str), "features isn't a str"
        features = ffi.new("char[]", features.encode("utf8"))
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``alpha`` isn't a :class:`int`.
        """
        assert isinstance(alpha, int), "alpha isn't a int"
        alpha = ffi.cast("guint16", alpha)
        temp = cls._init_pointer(
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
        :return:
            the Attribute.
        :raises: AssertionError
            When ``alpha`` isn't a :class:`int`.
        """
        assert isinstance(alpha, int), "alpha isn't a int"
        alpha = ffi.cast("guint16", alpha)
        temp = cls._init_pointer(
            pango.pango_attr_background_alpha_new(alpha),
        )
        temp.start_index = start_index
        temp.end_index = end_index
        return temp

    def copy(self) -> "Attribute":
        """
        Make a copy of an attribute.

        :return:
            the Attribute.
        """
        return Attribute._init_pointer(
            pango.pango_attribute_copy(self._pointer),
        )

    def __copy__(self) -> "Attribute":
        return self.copy()

    def __deepcopy__(self, memo) -> "Attribute":
        return self.copy()


class AttrList:
    """
    The :class:`AttrList` represents a list of attributes(:class:`Attribute`)
    that apply to a section of text. The attributes are, in general, allowed
    to overlap in an arbitrary fashion, however, if the attributes are
    manipulated only through :func:`AttrList.change()`, the overlap between
    properties will meet stricter criteria.

    In general, you should not use a single :class:`AttrList` for more than
    one paragraph of text due to internal structures.
    """

    def __init__(self) -> None:
        self._init_pointer(pango.pango_attr_list_new())

    def _init_pointer(self, pointer: ffi.CData):
        self._pointer = ffi.gc(pointer, pango.pango_attr_list_unref)

    def get_pointer(self) -> ffi.CData:
        """
        Returns the pointer to the AttrList

        :return:
            the pointer to the AttrList.
        """
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ffi.CData) -> "AttrList":
        """
        Instantiates a :class:`AttrList` from a pointer.

        :return:
            the AttrList.
        """
        if pointer == ffi.NULL:
            raise ValueError("Null pointer")
        self = object.__new__(cls)
        self._pointer = pointer
        return self

    def _ref(self) -> None:
        """
        Increase the reference count of the given attribute list by one.
        """
        self._pointer = pango.pango_attr_list_ref(self._pointer)

    def _unref(self) -> None:
        """
        Decrease the reference count of the given attribute list by one.
        If the result is zero, free the attribute list and the attributes
        it contains.
        """
        pango.pango_attr_list_unref(self._pointer)

    def copy(self) -> "AttrList":
        """
        Copy :class:`AttrList` and return an identical new.
        """
        return AttrList.from_pointer(pango.pango_attr_list_copy(self._pointer))

    def __copy__(self) -> "AttrList":
        return self.copy()

    def __deepcopy__(self, memo) -> "AttrList":
        return self.copy()

    def insert(self, attr: Attribute) -> None:
        """
        Insert the given attribute into the PangoAttrList. It will be inserted
        after all other attributes with a matching ``start_index``.

        :param attr:
            The :class:`Attribute` to insert.
        :raises: AssertionError
            When ``attr`` isn't a :class:`Attribute`.
        """
        assert isinstance(attr, Attribute), "attr isn't a Attribute"
        self._ref()
        pango.pango_attr_list_insert(self._pointer, attr._pointer)

    def insert_before(self, attr: Attribute) -> None:
        """
        Insert the given attribute into the PangoAttrList. It will be inserted
        before all other attributes with a matching ``start_index``.

        :param attr:
            The :class:`Attribute` to insert.
        :raises: AssertionError
            When ``attr`` isn't a :class:`Attribute`.
        """
        assert isinstance(attr, Attribute), "attr isn't a Attribute"
        self._ref()
        pango.pango_attr_list_insert_before(self._pointer, attr._pointer)

    def change(self, attr: Attribute) -> None:
        """
        Insert the given attribute into the :class:`AttrList`. It will replace
        any attributes of the same type on that segment and be merged with any
        adjoining attributes that are identical.

        This function is slower than :py:meth:`AttrList.insert` for creating
        an attribute list in order (potentially much slower for large lists).
        However, :py:meth:`AttrList.insert` is not suitable for continually
        changing a set of attributes since it never removes or combines
        existing attributes.

        :param attr:
            The :class:`Attribute` to insert.
        :raises: AssertionError
            When ``attr`` isn't a :class:`Attribute`.
        """
        assert isinstance(attr, Attribute), "attr isn't a Attribute"
        self._ref()
        pango.pango_attr_list_change(self._pointer, attr._pointer)

    def splice(self, attr_list: "AttrList", pos: int, length: int):
        """This function opens up a hole in ``self``, fills it in with attributes
        from the left, and then merges other on top of the hole.
        This operation is equivalent to stretching every attribute that applies
        at position pos in list by an amount len , and then calling
        :py:meth:`AttrList.change` with a copy of each attribute in other in
        sequence (offset in position by pos ).

        This operation proves useful for, for instance, inserting a pre-edit
        string in the middle of an edit buffer.


        :param attr_list: another :class:`AttrList`
        :type attr_list: AttrList
        :param pos: the position in ``self`` at which to insert other
        :type pos: int
        :param length:
            the length of the spliced segment. (Note that this must be
            specified since the attributes in other may only be present
            at some subsection of this range)
        :type length: int
        :raises: AssertionError
            When ``attr_list`` isn't a :class:`AttrList`.
            When ``pos`` isn't a :class:`int`
            When ``length`` isn't a :class:`int`
        """
        assert isinstance(attr_list, AttrList), "attr_list isn't a AttrList"
        assert isinstance(pos, int), "pos isn't a int"
        assert isinstance(length, int), "length isn't a int"
        length = ffi.cast("gint", length)
        pos = ffi.cast("gint", pos)
        pango.pango_attr_list_splice(
            self._pointer,
            attr_list._pointer,
            pos,
            length,
        )

    def __eq__(self, other: "AttrList") -> bool:
        if isinstance(other, AttrList):
            return bool(
                pango.pango_attr_list_equal(
                    self.get_pointer(),
                    other.get_pointer(),
                )
            )
        raise NotImplementedError

    # TODO: pango_attr_list_filter ()
