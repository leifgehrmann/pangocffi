"""
    pangocffi.ffi_instance_builder
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    generates an FFI for pangocffi
"""

import os
from pathlib import Path
from cffi import FFI
from typing import Optional


class FFIInstanceBuilder:

    def __init__(self, source: Optional[str] = None):
        self.source = source

    def generate(self) -> FFI:
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
        if self.source is not None:
            if ('PANGOCFFI_API_MODE' in os.environ and
                    int(os.environ['PANGOCFFI_API_MODE']) == 1):
                ffi.set_source_pkgconfig(
                    '_pangocffi',
                    ['pango', 'glib-2.0', 'pangoft2'],
                    """
                    #include "glib.h"
                    #include "glib-object.h"
                    #include "pango/pango.h"
                    #include "pango/pango-fontmap.h"
                    """,
                    sources=[]
                )
            else:
                ffi.set_source(self.source, None)

        return ffi
