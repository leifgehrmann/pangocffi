
from . import pango, ffi, PangoObject


class FontMetrics(PangoObject):
    """
    The :class:`FontMetrics` describes metrics about a font.
    """
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoFontMetrics"

    def _get_approximate_char_width(self) -> int:
        return pango.pango_font_metrics_get_approximate_char_width(
            self._pointer)

    approximate_char_width: int = property(_get_approximate_char_width)
    """
    The approximate character width, in Pango units.

    This is merely a representative value useful, for example, for determining
    the initial size for a window. Actual characters in text will be wider and
    narrower than this.
    """

    def _get_approximate_digit_width(self) -> int:
        return pango.pango_font_metrics_get_approximate_digit_width(
            self._pointer)

    approximate_digit_width: int = property(_get_approximate_digit_width)
    """
    The approximate digit width, in Pango units.

    This is merely a representative value useful, for example, for determining
    the initial size for a window. Actual digits in text can be wider or
    narrower than this, though this value is generally somewhat more accurate
    than the result of :attr:`approximate_char_width` for digits.
    """

    def _get_ascent(self) -> int:
        return pango.pango_font_metrics_get_ascent(
            self._pointer)

    ascent: int = property(_get_ascent)
    """
    The ascent, in Pango units.

    The ascent is the distance from the baseline to the logical top of a line
    of text. (The logical top may be above or below the top of the actual
    drawn ink. It is necessary to lay out the text to figure where the ink
    will be.).
    """

    def _get_descent(self) -> int:
        return pango.pango_font_metrics_get_descent(
            self._pointer)

    descent: int = property(_get_descent)
    """
    The descent, in Pango units.

    The descent is the distance from the baseline to the logical bottom of a
    line of text. (The logical bottom may be above or below the bottom of the
    actual drawn ink. It is necessary to lay out the text to figure where the
    ink will be.).
    """

    def _get_height(self) -> int:
        return pango.pango_font_metrics_get_height(
            self._pointer)

    height: int = property(_get_height)
    """
    The height, in Pango units.

    The line height is the recommended distance between successive baselines
    in wrapped text using this font.

    If the line height is not available, 0 is returned.
    """

    def _get_strikethrough_position(self) -> int:
        return pango.pango_font_metrics_get_strikethrough_position(
            self._pointer)

    strikethrough_position: int = property(_get_strikethrough_position)
    """
    The suggested strikethrough position, in Pango units.

    The value returned is the distance *above* the baseline of the top of the
    strikethrough.
    """

    def _get_strikethrough_thickness(self) -> int:
        return pango.pango_font_metrics_get_strikethrough_thickness(
            self._pointer)

    strikethrough_thickness: int = property(_get_strikethrough_thickness)
    """
    The suggested strikethrough thickness, in Pango units.
    """

    def _get_underline_position(self) -> int:
        return pango.pango_font_metrics_get_underline_position(
            self._pointer)

    underline_position: int = property(_get_underline_position)
    """
    The suggested underline position, in Pango units.

    The value returned is the distance *above* the baseline of the top of the
    underline. Since most fonts have underline positions beneath the baseline,
    this value is typically negative.
    """

    def _get_underline_thickness(self) -> int:
        return pango.pango_font_metrics_get_underline_thickness(
            self._pointer)

    underline_thickness: int = property(_get_underline_thickness)
    """
    The suggested underline thickness, in Pango units.
    """
