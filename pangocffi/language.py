from typing import Optional, List

from . import pango, ffi, PangoObject


class Language(PangoObject):
    """
    The :class:`Language` represents a pango Language.
    """
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoLanguage"

    @staticmethod
    def from_string(lang: Optional[str]) -> Optional['Language']:
        """
        Create a language from a string descriptor.

        :param lang:
            A string representing a language tag.
        :return:
            A Language.

            The return value can be ``None``.
        """
        if lang is not None:
            lang = ffi.new("char[]", lang.encode("utf-8"))
        else:
            lang = ffi.NULL
        lang_pointer = pango.pango_language_from_string(lang)
        if lang_pointer == ffi.NULL:
            return None
        return Language.from_pointer(
            pango.pango_language_from_string(lang)
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
    def preferred() -> Optional[List['Language']]:
        """
        Return the preferred language
        """
        langs_pointer = Language._pango_language_get_preferred()
        if langs_pointer == ffi.NULL:
            return None

        return [(Language.from_pointer(langs_pointer[i]))
                for i in range(len(langs_pointer))]

    @staticmethod
    def _pango_language_get_preferred():
        """
        This method exists so the value can be mocked.
        """
        return pango.pango_language_get_preferred()

    def matches(self, range_list: str) -> bool:
        """
        Return if the language matches that in `range_list`.

        :param desc:`range_list`
            the language description.
        """
        range_list = ffi.new("char[]", range_list.encode("utf-8"))
        return bool(pango.pango_language_matches(self._pointer, range_list))

    def to_string(self) -> str:
        """
        Describe the language as a string.
        """
        return ffi.string(
            pango.pango_language_to_string(self._pointer)
        ).decode("utf-8")
