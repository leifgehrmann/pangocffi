import unittest
from unittest.mock import patch

from pangocffi import Language, ffi


class TestLanguage(unittest.TestCase):

    def test_from_string(self):
        lang = Language.from_string('pt_BR')
        assert isinstance(lang, Language)

    def test_from_string_invalid_locale(self):
        lang = Language.from_string(None)
        assert lang is None

    def test_default(self):
        lang = Language.default()
        assert isinstance(lang, Language)
        assert isinstance(lang.to_string(), str)
        assert len(lang.to_string()) > 0

    def test_preferred_with_no_mock(self):
        langs = Language.preferred()
        assert langs is None or len(langs) > 0

    def test_preferred_with_null_mock(self):
        with patch(
                'pangocffi.language.Language._pango_language_get_preferred'
        ) as mock_func:
            mock_func.return_value = ffi.NULL
            langs = Language.preferred()
            assert langs is None

    def test_preferred_with_mock_list(self):
        mock_language_a = Language.from_string('en')
        mock_language_b = Language.from_string('de')
        mock_langs_pointer = ffi.new("PangoLanguage*[2]", [])
        mock_langs_pointer[0] = mock_language_a.pointer
        mock_langs_pointer[1] = mock_language_b.pointer

        with patch(
                'pangocffi.language.Language._pango_language_get_preferred'
        ) as mock_func:
            mock_func.return_value = mock_langs_pointer
            langs = Language.preferred()
            assert langs is not None
            assert len(langs) == 2
            assert langs[0].to_string() == 'en'
            assert langs[1].to_string() == 'de'

    def test_get_sample_string(self):
        lang = Language.from_string('en-US')
        sample_string = lang.get_sample_string()
        assert len(sample_string) > 0

    def test_matches(self):
        lang = Language.from_string('pt_BR')
        assert lang.matches('*')
        assert lang.matches('pt')
        assert lang.matches('pt;de')
        assert lang.matches('pt:de')
        assert lang.matches('pt,de')
        assert lang.matches('pt-br')
        assert lang.matches('pt_BR') is False
        assert lang.matches('pt-de') is False
        assert lang.matches('de') is False
        assert lang.matches('de;se') is False
        assert lang.matches('de:se') is False
        assert lang.matches('de,se') is False

    def test_to_string(self):
        lang = Language.from_string('pt_BR')
        assert lang.to_string() == 'pt-br'

    def test_equal(self):
        lang_a = Language.from_string('pt_BR')
        lang_b = Language.from_string('pt-br')
        lang_c = Language.from_string('de-de')
        assert lang_a == lang_b
        assert lang_a != lang_c
