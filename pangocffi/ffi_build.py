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

# cffi definitions, in the order outlined in https://developer.gnome.org/pango/stable
ffi = FFI()
ffi.set_source('pangocffi._generated.ffi', None)
ffi.cdef('''
    /* === GLib === */
    
    typedef void* gpointer;
    void g_object_unref (gpointer object);

    /* === Pango === */
    
    /* --- Rendering --- */
    typedef ... PangoContext;
    
    PangoContext * pango_context_new (void);
    
    /* --- Glyph Storage --- */
    typedef struct {
        int x;
        int y;
        int width;
        int height;
    } PangoRectangle;
    int pango_units_from_double (double d);
    double pango_units_to_double (int d);
    
    /* --- Layout Objects --- */
    typedef ... PangoLayout;
    
    typedef enum {
        PANGO_ELLIPSIZE_NONE,
        PANGO_ELLIPSIZE_START,
        PANGO_ELLIPSIZE_MIDDLE,
        PANGO_ELLIPSIZE_END
    } PangoEllipsizeMode;
    
    typedef enum {
        PANGO_ALIGN_LEFT,
        PANGO_ALIGN_CENTER,
        PANGO_ALIGN_RIGHT
    } PangoAlignment;
    
    PangoLayout * pango_layout_new (PangoContext *context);
    PangoContext * pango_layout_get_context (PangoLayout *layout);
    void pango_layout_set_markup (PangoLayout *layout, const char *text, int length);
    void pango_layout_set_width (PangoLayout *layout, int width);
    int pango_layout_get_width (PangoLayout *layout);
    void pango_layout_set_height (PangoLayout *layout, int height);
    int pango_layout_get_height (PangoLayout *layout);
    void pango_layout_set_alignment (PangoLayout *layout, PangoAlignment alignment);
    PangoAlignment pango_layout_get_alignment(PangoLayout *layout);
    void pango_layout_get_extents (PangoLayout *layout, PangoRectangle *ink_rect, PangoRectangle *logical_rect);
    
    /* --- Version Checking --- */
    int pango_version (void);
    const char * pango_version_string (void);
    const char * pango_version_check (int required_major, int required_minor, int required_micro);
''')

if __name__ == '__main__':
    ffi.compile()
