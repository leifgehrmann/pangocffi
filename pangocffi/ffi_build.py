"""
    pangocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings

"""

import sys
from pathlib import Path
from cffi import FFI

sys.path.append(str(Path(__file__).parent))

# Create an empty _generated folder if needed
(Path(__file__).parent / '_generated').mkdir(exist_ok=True)

# Read the CFFI definitions
cdefs_glib_file = open(str(Path(__file__).parent / 'cdefs_glib.txt'), 'r')
cdefs_glib = cdefs_glib_file.read()
cdefs_pango_file = open(str(Path(__file__).parent / 'cdefs_pango.txt'), 'r')
cdefs_pango = cdefs_pango_file.read()

# cffi definitions, in the order outlined in:
# https://developer.gnome.org/pango/stable
ffi = FFI()
ffi.set_source('pangocffi._generated.ffi', None)
ffi.cdef(cdefs_glib)
ffi.cdef(cdefs_pango)

if __name__ == '__main__':
    ffi.compile()
