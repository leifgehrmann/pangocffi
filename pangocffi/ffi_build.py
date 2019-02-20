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

# Primary cffi definitions
ffi = FFI()
ffi.set_source('pangocffi._generated.ffi', None)
ffi.cdef('''
    typedef ... PangoLayout;
    typedef struct {
        int x;
        int y;
        int width;
        int height;
    } PangoRectangle;
    typedef enum {
        PANGO_ALIGN_LEFT,
        PANGO_ALIGN_CENTER,
        PANGO_ALIGN_RIGHT
    } PangoAlignment;
    int pango_units_from_double (double d);
    int pango_units_to_double (int d);
    void pango_layout_set_width (PangoLayout *layout, int width);
    void pango_layout_set_alignment (
        PangoLayout *layout, PangoAlignment alignment);
    void pango_layout_set_markup (
        PangoLayout *layout, const char *text, int length);
    int pango_layout_get_width (PangoLayout *layout);
    void pango_layout_get_extents (PangoLayout *layout, PangoRectangle *ink_rect, PangoRectangle *logical_rect);
    int pango_version (void);
    const char* pango_version_string (void);
''')

if __name__ == '__main__':
    ffi.compile()
