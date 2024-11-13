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

        The language tag must be in a RFC-3066 format.

        This function first canonicalizes the string by converting it to
        lowercase, mapping ``_`` to ``-``, and stripping all characters other
        than letters and ``-``.

        :param lang:
            A string representing a language tag.

            The argument can be ``None``.
        :return:
            A :class:`Language`.

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
        Returns the :class:`Language` for the current locale of the process.

        On Unix systems, this is the return value is derived from
        ``setlocale`` (``LC_CTYPE``, ``NULL``), and the user can affect this
        through the environment variables LC_ALL, LC_CTYPE or LANG (checked in
        that order). The locale string typically is in the form lang_COUNTRY,
        where lang is an ISO-639 language code, and COUNTRY is an ISO-3166
        country code. For instance, sv_FI for Swedish as written in Finland or
        pt_BR for Portuguese as written in Brazil.

        On Windows, the C library does not use any such environment variables,
        and setting them won’t affect the behavior of functions like ctime().
        The user sets the locale through the Regional Options in the Control
        Panel. The C library (in the setlocale() function) does not use country
        and language codes, but country and language names spelled out in
        English. However, this function does check the above environment
        variables, and does return a Unix-style locale string based on either
        said environment variables or the thread’s current locale.

        Your application should call ``setlocale(LC_ALL, "")`` for the user
        settings to take effect. GTK does this in its initialization functions
        automatically (by calling gtk_set_locale()). See the ``setlocale()``
        manpage for more details.

        Note that the default language can change over the life of an
        application.

        Also note that this function will not do the right thing if you use
        per-thread locales with uselocale(). In that case, you should just call
        :meth:`from_string()` yourself.

        :return:
            The default language as a :class:`Language`.
        """
        return Language.from_pointer(
            pango.pango_language_get_default()
        )

    @staticmethod
    def preferred() -> Optional[List['Language']]:
        """
        Returns the list of languages that the user prefers.

        The list is specified by the ``PANGO_LANGUAGE`` or ``LANGUAGE``
        environment variables, in order of preference. Note that this list does
        not necessarily include the language returned by :meth:`default()`.

        When choosing language-specific resources, such as the sample text
        returned by :meth:`get_sample_string()`, you should first try
        the default language, followed by the languages returned by this
        function.

        :return:
            A list of :class:`Language`.

            The return value can be ``None``.
        """
        langs_pointer = Language._pango_language_get_preferred()
        if langs_pointer == ffi.NULL:
            return None

        return [(Language.from_pointer(langs_pointer[i]))
                for i in range(len(langs_pointer))]

    @staticmethod
    def _pango_language_get_preferred():
        """
        This method exists so the preferred languages can be mocked in tests.
        """
        return pango.pango_language_get_preferred()

    def get_sample_string(self) -> str:
        """
        Get a string that is representative of the characters needed to render
        a particular language.

        The sample text may be a pangram, but is not necessarily. It is chosen
        to be demonstrative of normal text in the language, as well as exposing
        font feature requirements unique to the language. It is suitable for
        use as sample text in a font selection dialog.

        If Pango does not have a sample string for language, the classic
        “The quick brown fox…” is returned. This can be detected by comparing
        the returned pointer value to that returned for (non-existent) language
        code “xx”. That is, compare to::

            Language('xx').get_sample_string()

        :return:
            The sample string.
        """
        return ffi.string(
            pango.pango_language_get_sample_string(self._pointer)
        ).decode("utf-8")

    def matches(self, range_list: str) -> bool:
        """
        Checks if a language tag matches one of the elements in a list of
        language ranges.

        A language tag is considered to match a range in the list if the range
        is ``*``, the range is exactly the tag, or the range is a prefix of the
        tag, and the character after it in the tag is ``-``.

        :param range_list:
            A list of language ranges, separated by ``;``, ``:``, ``,``, or
            space characters. Each element must either be ``*``, or a RFC 3066
            language range canonicalized as by :meth:`from_string()`.
        :return:
            ``True`` if a match was found.
        """
        range_list = ffi.new("char[]", range_list.encode("utf-8"))
        return bool(pango.pango_language_matches(self._pointer, range_list))

    def to_string(self) -> str:
        """
        Gets the RFC-3066 format string representing the given language tag.

        :return:
            The string.
        """
        return ffi.string(
            pango.pango_language_to_string(self._pointer)
        ).decode("utf-8")
