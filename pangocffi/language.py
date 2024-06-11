from . import pango, ffi, PangoObject


class Language(PangoObject):
    """
    The :class:`Language` represents a pango Language.
    """
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoLanguage"

    @staticmethod
    def from_string(lang: str) -> 'Language':
        """
        Create a language from a string descriptor.

        :param desc:`lang`
            the language description.
        """
        return Language.from_pointer(
            pango.pango_language_from_string(str)
        )

    @staticmethod
    def default() -> 'Language':
        """
        Return the default language
        """
        return Language.from_pointer(
            pango.pango_language_get_default()
        )

    @staticmethod
    def preferred() -> 'Language':
        """
        Return the preferred language
        """
        return Language.from_pointer(
            pango.pango_language_get_preferred()
        )

    def matches(self, range_list: str) -> bool:
        """
        Return if the language matches that in `range_list`.

        :param desc:`range_list`
            the language description.
        """
        return pango.pango_language_matches(self._pointer, range_list)

    def to_string(self) -> str:
        """
        Describe the language as a string.
        """
        return pango.pango_language_to_string(self._pointer)

