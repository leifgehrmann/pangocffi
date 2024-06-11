
from . import pango, ffi, PangoObject


class FontMetrics(PangoObject):
    """
    The :class:`FontMetrics` describes metrics about a font.
    """
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoFontMetrics"

    def approximate_char_width(self) -> int:
        return pango.pango_font_metrics_get_approximate_char_width(self._pointer)

    def approximate_digit_width(self) -> int:
        return pango.pango_font_metrics_get_approximate_digit_width(self._pointer)

    def ascent(self) -> int:
        return pango.pango_font_metrics_get_ascent(self._pointer)

    def descent(self) -> int:
        return pango.pango_font_metrics_get_descent(self._pointer)

    def height(self) -> int:
        return pango.pango_font_metrics_get_height(self._pointer)

    def strikethrough_position(self) -> int:
        return pango.pango_font_metrics_get_strikethrough_position(self._pointer)

    def strikethrough_thickness(self) -> int:
        return pango.pango_font_metrics_get_strikethrough_thickness(self._pointer)

    def underline_position(self) -> int:
        return pango.pango_font_metrics_get_underline_position(self._pointer)

    def underline_thickness(self) -> int:
        return pango.pango_font_metrics_get_underline_thickness(self._pointer)

