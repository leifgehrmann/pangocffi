from typing import Optional, Union
from . import pango, ffi, PangoObject
from . import Style, Variant, Weight, Stretch, Gravity


class FontDescription(PangoObject):
    """
    The :class:`FontDescription` represents the description of an ideal font.
    These structures are used both to list what fonts are available on the
    system and also for specifying the characteristics of a font to load.
    """

    _INIT_METHOD = pango.pango_font_description_new
    _GC_METHOD = pango.pango_font_description_free
    _COPY_METHOD = pango.pango_font_description_copy

    def _get_family(self) -> Optional[str]:
        family_pointer = pango.pango_font_description_get_family(self._pointer)
        if family_pointer == ffi.NULL:
            return None
        return ffi.string(family_pointer).decode()

    def _set_family(self, family: str) -> None:
        family_pointer = ffi.new('char[]', family.encode('utf8'))
        pango.pango_font_description_set_family(self._pointer, family_pointer)

    family: Optional[str] = property(_get_family, _set_family)
    """
    The family name of the font description. This represents a font family of
    related font styles, and will resolve to a particular :class:`FontFamily`.
    In some uses of :class:`FontDescription`, it is also possible to use a
    comma-separated list of family names for this field.
    """

    def _get_style(self) -> Style:
        return Style(pango.pango_font_description_get_style(self._pointer))

    def _set_style(self, style: Style) -> None:
        pango.pango_font_description_set_style(self._pointer, style.value)

    style: Style = property(_get_style, _set_style)
    """
    The slant style of the font description.

    Most fonts will either have an italic style or an oblique style, but not
    both, and font matching in Pango will match italic specifications with
    oblique fonts and vice-versa if an exact match is not found.
    """

    def _get_variant(self) -> Variant:
        return Variant(pango.pango_font_description_get_variant(self._pointer))

    def _set_variant(self, variant: Variant) -> None:
        pango.pango_font_description_set_variant(self._pointer, variant.value)

    variant: Variant = property(_get_variant, _set_variant)
    """
    The variant of the font description, which describes whether the font
    is normal or small caps.
    """

    def _get_weight(self) -> int:
        return pango.pango_font_description_get_weight(self._pointer)

    def _set_weight(self, weight: Union[Weight, int]) -> None:
        if isinstance(weight, Weight):
            weight = weight.value
        pango.pango_font_description_set_weight(self._pointer, weight)

    weight: Union[Weight, int] = property(_get_weight, _set_weight)

    def _get_stretch(self) -> Stretch:
        return Stretch(pango.pango_font_description_get_stretch(self._pointer))

    def _set_stretch(self, stretch: Stretch) -> None:
        pango.pango_font_description_set_stretch(self._pointer, stretch.value)

    stretch: Stretch = property(_get_stretch, _set_stretch)
    """
    The stretch of the font description, which specifies how narrow or
    wide the font should be.
    """

    def _set_size(self, size: int) -> None:
        pango.pango_font_description_set_size(self._pointer, size)

    def _get_size(self) -> int:
        """
        Returns the size field of a font description.

        :return:
            the size field for the font description in points or device units.
            You must call :meth:`get_size_is_absolute()` to find out which is
            the case. Returns 0 if the size field has not previously been set
            or it has been set to 0 explicitly.
        """
        return pango.pango_font_description_get_size(self._pointer)

    size = property(_get_size, _set_size)
    """
    The size field of a font description in fractional points, scaled by
    ``PANGO_SCALE``. (That is, a size value of ``10 * PANGO_SCALE`` is a
    10 point font). The conversion factor between points and device units
    depends on system configuration and the output device. For screen display,
    a logical DPI of 96 is common, in which case a 10 point font corresponds
    to a ``10 * (96 / 72) = 13.3`` pixel font. Use :meth:`set_absolute_size()`
    if you need a particular size in device units.
    """

    @property
    def size_is_absolute(self) -> bool:
        """
        Determines whether the size of the font is in points (not absolute) or
        device units (absolute). See :attr:`size` and
        :meth:`set_absolute_size()`.

        :return:
            whether the size for the font description is in device units.
        """
        return pango.pango_font_description_get_size_is_absolute(self._pointer)

    def _get_gravity(self) -> Gravity:
        return Gravity(pango.pango_font_description_get_gravity(self._pointer))

    def _set_gravity(self, gravity: Gravity) -> None:
        pango.pango_font_description_set_gravity(self._pointer, gravity.value)

    gravity: Gravity = property(_get_gravity, _set_gravity)
    """
    Sets the gravity of the font description, which specifies how the glyphs
    should be rotated. If gravity is ``Gravity.AUTO``, this actually unsets
    the gravity mask on the font description.
    """

    def set_absolute_size(self, size: float) -> None:
        """
        Sets the size field of a font description, in device units. There are
        ``PANGO_SCALE`` Pango units in one device unit. For an output backend
        where a device unit is a pixel, a size value of ``10 * PANGO_SCALE``
        gives a 10 pixel font. See :attr:`size`.
        """
        pango.pango_font_description_set_absolute_size(self._pointer, size)
