"""
    pangocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings for pangocffi

"""

import platform
import sys
from setuptools.errors import CCompilerError, ExecError, PlatformError
from pathlib import Path
from warnings import warn

from cffi import FFI
from cffi.error import PkgConfigError, VerificationError

sys.path.append(str(Path(__file__).parent))


def ffi_for_mode(mode):
    # Read the C definitions
    c_definitions_glib_file = open(
        str(Path(__file__).parent / 'c_definitions_glib.txt'),
        'r'
    )
    c_definitions_pango_file = open(
        str(Path(__file__).parent / 'c_definitions_pango.txt'),
        'r'
    )
    c_definitions_glib = c_definitions_glib_file.read()
    c_definitions_pango = c_definitions_pango_file.read()

    ffi = FFI()
    # Mirror the GType setup in gobject/gtypes.h
    if ffi.sizeof('void*') > ffi.sizeof('long'):
        ffi.cdef('typedef unsigned int* GType;')
    else:
        ffi.cdef('typedef unsigned long GType;')
    ffi.cdef(c_definitions_glib)
    ffi.cdef(c_definitions_pango)
    if mode == "api":
        ffi.set_source_pkgconfig(
            "_pangocffi",
            ['pango', 'glib-2.0', 'pangoft2'] +
            (['pangoxft'] if platform.system() == 'Linux' else []),
            r"""
            #include "glib.h"
            #include "glib-object.h"
            #include "pango/pango.h"
            #include "pango/pango-fontmap.h"

            #include <stdio.h>
            #if PANGO_VERSION < G_ENCODE_VERSION(1, 54)
            int pango_item_get_char_offset (
              PangoItem* item) {
                fprintf(stderr, "Unimplemented!!\n");
                return -1;
            }
            #endif
            #if PANGO_VERSION < G_ENCODE_VERSION(1, 52)
            PangoFont*
            pango_font_map_reload_font (
              PangoFontMap* fontmap,
              PangoFont* font,
              double scale,
              PangoContext* context,
              const char* variations) {
                fprintf(stderr, "Unimplemented!!\n");
                return NULL;
            }

            #endif
            """,
            sources=[]
        )
    else:
        ffi.set_source("_pangocffi", None)
    return ffi


def build_ffi():
    """
    This will be called from setup() to return an FFI
    which it will compile - work out here which type is
    possible and return it.
    """
    try:
        ffi_api = ffi_for_mode("api")
        ffi_api.compile(verbose=True)
        return ffi_api
    except (CCompilerError, ExecError, PlatformError,
            PkgConfigError, VerificationError) as e:
        warn("Falling back to precompiled python mode: {}".format(str(e)))

        ffi_abi = ffi_for_mode("abi")
        ffi_abi.compile(verbose=True)
        return ffi_abi


if __name__ == '__main__':
    ffi = build_ffi()
    ffi.compile()
