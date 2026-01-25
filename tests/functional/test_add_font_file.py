import sys
from pathlib import Path
from typing import Any, TypeAlias

import pytest

from pangocffi import ffi, pango, pango_version
from tests.context_creator import ContextCreator

PangoFontMap_ptr: TypeAlias = Any


needs_pango_156 = pytest.mark.skipif(
    pango_version() < 15600, reason="needs pango >= 1.56"
)


skip_macos = pytest.mark.skipif(
    sys.platform == 'darwin',
    reason="Adding font files not supported for PangoCairoCoreTextFontMap"
)


TEST_FONT_PATH = Path(__file__).parent / "Untitled1.ttf"
TEST_FONT_FAMILY_NAME = "Untitled1"


@needs_pango_156
@skip_macos
def test_pango_font_map_add_font_file():
    context_creator = ContextCreator.create_surface_without_output()
    fontmap = context_creator.pangocairo.pango_cairo_font_map_new()

    assert TEST_FONT_FAMILY_NAME not in _all_family_names(fontmap)

    _pango_font_map_add_font_file(fontmap, str(TEST_FONT_PATH))

    assert TEST_FONT_FAMILY_NAME in _all_family_names(fontmap)


@needs_pango_156
@skip_macos
def test_pango_font_map_add_font_file_error():
    context_creator = ContextCreator.create_surface_without_output()
    fontmap = context_creator.pangocairo.pango_cairo_font_map_new()

    with pytest.raises(ValueError) as e:
        _pango_font_map_add_font_file(fontmap, "/not/a/font/filename.xxx")
    # Linux and Windows return these errors, respectively
    assert e.match(
        r"(Adding.* /not/a/font/filename.xxx .*failed)|"
        r"(Specified font file '/not/a/font/filename.xxx' does not exist)")


def _pango_font_map_add_font_file(fontmap: PangoFontMap_ptr, filename: str):
    filename = ffi.new("char[]", filename.encode())
    error = ffi.new("GError**")
    if not pango.pango_font_map_add_font_file(fontmap, filename, error):
        raise ValueError(ffi.string(error[0][0].message).decode("utf8"))


def _all_family_names(fontmap: PangoFontMap_ptr):
    families = ffi.new("PangoFontFamily***")
    n_families = ffi.new("int*")
    pango.pango_font_map_list_families(fontmap, families, n_families)
    for i in range(n_families[0]):
        name = pango.pango_font_family_get_name(families[0][i])
        yield ffi.string(name).decode("utf8")
