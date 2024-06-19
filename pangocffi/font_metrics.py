
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

    def _get_approximate_digit_width(self) -> int:
        return pango.pango_font_metrics_get_approximate_digit_width(
            self._pointer)

    approximate_digit_width: int = property(_get_approximate_digit_width)

    def _get_ascent(self) -> int:
        return pango.pango_font_metrics_get_ascent(
            self._pointer)

    ascent: int = property(_get_ascent)

    def _get_descent(self) -> int:
        return pango.pango_font_metrics_get_descent(
            self._pointer)

    descent: int = property(_get_descent)

    def _get_height(self) -> int:
        return pango.pango_font_metrics_get_height(
            self._pointer)

    height: int = property(_get_height)

    def _get_strikethrough_position(self) -> int:
        return pango.pango_font_metrics_get_strikethrough_position(
            self._pointer)

    strikethrough_position: int = property(_get_strikethrough_position)

    def _get_strikethrough_thickness(self) -> int:
        return pango.pango_font_metrics_get_strikethrough_thickness(
            self._pointer)

    strikethrough_thickness: int = property(_get_strikethrough_thickness)

    def _get_underline_position(self) -> int:
        return pango.pango_font_metrics_get_underline_position(
            self._pointer)

    underline_position: int = property(_get_underline_position)

    def _get_underline_thickness(self) -> int:
        return pango.pango_font_metrics_get_underline_thickness(
            self._pointer)

    underline_thickness: int = property(_get_underline_thickness)
