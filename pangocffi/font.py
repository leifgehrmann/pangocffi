from . import pango, ffi, PangoObject, FontMetrics, Language


class Font(PangoObject):
    """
    The :class:`Font` represents a loaded font.
    """
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoFont"

    def get_metrics(self, language: Language) -> FontMetrics:
        """
        Return font metrics for the font.
        """
        return FontMetrics.from_pointer(
            pango.pango_font_get_metrics(self._pointer, language._pointer)
        )
