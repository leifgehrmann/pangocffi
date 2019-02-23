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
    typedef int gint;
    typedef int gboolean;
    void g_object_unref (gpointer object);

    /* === Pango === */
    
    /* --- Rendering --- */
    typedef ... PangoContext;
    typedef ... PangoFontDescription;
    
    PangoContext * pango_context_new (void);
    PangoFontDescription * pango_context_get_font_description (PangoContext *context);
    void pango_context_set_font_description (PangoContext *context, const PangoFontDescription *desc);
    
    /* --- Fonts --- */
    typedef enum {
        PANGO_STYLE_NORMAL,
        PANGO_STYLE_OBLIQUE,
        PANGO_STYLE_ITALIC
    } PangoStyle;
    typedef enum {
        PANGO_WEIGHT_THIN,
        PANGO_WEIGHT_ULTRALIGHT,
        PANGO_WEIGHT_LIGHT,
        PANGO_WEIGHT_SEMILIGHT,
        PANGO_WEIGHT_BOOK,
        PANGO_WEIGHT_NORMAL,
        PANGO_WEIGHT_MEDIUM,
        PANGO_WEIGHT_SEMIBOLD,
        PANGO_WEIGHT_BOLD,
        PANGO_WEIGHT_ULTRABOLD,
        PANGO_WEIGHT_HEAVY,
        PANGO_WEIGHT_ULTRAHEAVY
    } PangoWeight;
    typedef enum {
        PANGO_VARIANT_NORMAL,
        PANGO_VARIANT_SMALL_CAPS
    } PangoVariant;
    typedef enum {
        PANGO_STRETCH_ULTRA_CONDENSED,
        PANGO_STRETCH_EXTRA_CONDENSED,
        PANGO_STRETCH_CONDENSED,
        PANGO_STRETCH_SEMI_CONDENSED,
        PANGO_STRETCH_NORMAL,
        PANGO_STRETCH_SEMI_EXPANDED,
        PANGO_STRETCH_EXPANDED,
        PANGO_STRETCH_EXTRA_EXPANDED,
        PANGO_STRETCH_ULTRA_EXPANDED
    } PangoStretch;
    typedef enum {
        PANGO_FONT_MASK_FAMILY,
        PANGO_FONT_MASK_STYLE,
        PANGO_FONT_MASK_VARIANT,
        PANGO_FONT_MASK_WEIGHT,
        PANGO_FONT_MASK_STRETCH,
        PANGO_FONT_MASK_SIZE,
        PANGO_FONT_MASK_GRAVITY
    } PangoFontMask;
    typedef enum {
        PANGO_GRAVITY_SOUTH,
        PANGO_GRAVITY_EAST,
        PANGO_GRAVITY_NORTH,
        PANGO_GRAVITY_WEST,
        PANGO_GRAVITY_AUTO
    } PangoGravity;
    typedef enum {
        PANGO_GRAVITY_HINT_NATURAL,
        PANGO_GRAVITY_HINT_STRONG,
        PANGO_GRAVITY_HINT_LINE
    } PangoGravityHint;
    
    PangoFontDescription * pango_font_description_new (void);
    void pango_font_description_free (PangoFontDescription *desc);
    void pango_font_description_set_family (PangoFontDescription *desc, const char *family);
    const char * pango_font_description_get_family (const PangoFontDescription *desc);
    void pango_font_description_set_style (PangoFontDescription *desc, PangoStyle style);
    PangoStyle pango_font_description_get_style (const PangoFontDescription *desc);
    void pango_font_description_set_variant (PangoFontDescription *desc, PangoVariant variant);
    PangoVariant pango_font_description_get_variant (const PangoFontDescription *desc);
    void pango_font_description_set_weight (PangoFontDescription *desc, PangoWeight weight);
    PangoWeight pango_font_description_get_weight (const PangoFontDescription *desc);
    void pango_font_description_set_stretch (PangoFontDescription *desc, PangoStretch stretch);
    PangoStretch pango_font_description_get_stretch (const PangoFontDescription *desc);
    void pango_font_description_set_size (PangoFontDescription *desc, gint size);
    gint pango_font_description_get_size (const PangoFontDescription *desc);
    void pango_font_description_set_absolute_size (PangoFontDescription *desc, double size);
    gboolean pango_font_description_get_size_is_absolute (const PangoFontDescription *desc);
    void pango_font_description_set_gravity (PangoFontDescription *desc, PangoGravity gravity);
    PangoGravity pango_font_description_get_gravity (const PangoFontDescription *desc);
    
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
    void pango_layout_set_text (PangoLayout *layout, const char *text, int length);
    void pango_layout_set_markup (PangoLayout *layout, const char *markup, int length);
    void pango_layout_set_font_description (PangoLayout *layout, const PangoFontDescription *desc);
    const PangoFontDescription * pango_layout_get_font_description (PangoLayout *layout);
    void pango_layout_set_width (PangoLayout *layout, int width);
    int pango_layout_get_width (PangoLayout *layout);
    void pango_layout_set_height (PangoLayout *layout, int height);
    int pango_layout_get_height (PangoLayout *layout);
    void pango_layout_set_alignment (PangoLayout *layout, PangoAlignment alignment);
    PangoAlignment pango_layout_get_alignment(PangoLayout *layout);
    void pango_layout_get_extents (PangoLayout *layout, PangoRectangle *ink_rect, PangoRectangle *logical_rect);
    void pango_layout_get_size (PangoLayout *layout, int *width, int *height);
    
    /* --- Version Checking --- */
    int pango_version (void);
    const char * pango_version_string (void);
    const char * pango_version_check (int required_major, int required_minor, int required_micro);
''')

if __name__ == '__main__':
    ffi.compile()
