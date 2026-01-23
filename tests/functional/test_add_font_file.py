from pathlib import Path
from typing import Any, TypeAlias

import pytest

from pangocffi import ffi, pango, pango_version
from tests.context_creator import ContextCreator

PangoFontMap_ptr: TypeAlias = Any


needs_pango_156 = pytest.mark.skipif(
    pango_version() < 15600, reason="needs pango >= 1.56"
)


TEST_FONT_PATH = Path(__file__).parent / "Untitled1.ttf"
TEST_FONT_FAMILY_NAME = "Untitled1"


@needs_pango_156
def test_pango_font_map_add_font_file():
    context_creator = ContextCreator.create_surface_without_output()
    fontmap = context_creator.pangocairo.pango_cairo_font_map_new()

    assert TEST_FONT_FAMILY_NAME not in _all_family_names(fontmap)

    assert _pango_font_map_add_font_file(fontmap, str(TEST_FONT_PATH))

    assert TEST_FONT_FAMILY_NAME in _all_family_names(fontmap)


def _pango_font_map_add_font_file(fontmap: PangoFontMap_ptr, filename: str):
    filename = ffi.new("char[]", filename.encode())
    success = pango.pango_font_map_add_font_file(fontmap, filename, ffi.NULL)
    return bool(success)


def _all_family_names(fontmap: PangoFontMap_ptr):
    families = ffi.new("PangoFontFamily***")
    n_families = ffi.new("int*")
    pango.pango_font_map_list_families(fontmap, families, n_families)
    for i in range(n_families[0]):
        name = pango.pango_font_family_get_name(families[0][i])
        yield ffi.string(name).decode("utf8")
