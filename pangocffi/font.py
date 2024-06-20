from typing import Optional

from . import pango, ffi, PangoObject, FontMetrics, Language


class Font(PangoObject):
    """
    The :class:`Font` represents a loaded font.
    """
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoFont"

    def get_metrics(self, language: Optional[Language] = None) -> FontMetrics:
        """
        Gets overall metric information for a font.

        Since the metrics may be substantially different for different scripts,
        a language tag can be provided to indicate that the metrics should be
        retrieved that correspond to the script(s) used by that language.

        :param language:
            Language tag used to determine which script to get the metrics for,
            or ``None`` to indicate to get the metrics for the entire font.
        :return:
            A :class:`FontMetrics` object.
        """
        language_pointer = ffi.NULL
        if language is not None:
            language_pointer = language._pointer

        return FontMetrics.from_pointer(
            pango.pango_font_get_metrics(self._pointer, language_pointer)
        )
