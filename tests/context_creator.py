import sys

import pangocffi
from pangocffi import Context
from pangocffi.ffi_build import ffi as ffi_builder
from cffi import FFI
import ctypes


def _dlopen(ffi, *names):
    """Try various names for the same library, for different platforms."""
    for name in names:
        for lib_name in (name, 'lib' + name):
            try:
                path = ctypes.util.find_library(lib_name)
                lib = ffi.dlopen(path or lib_name)
                if lib:
                    return lib
            except OSError:
                pass
    raise OSError("dlopen() failed to load a library: %s" % ' / '.join(names))


class ContextCreator(object):

    # CFFIs
    ffi = None
    cairo = None
    pangocairo = None

    # Surface pointers
    cairo_surface = None

    # Context pointers (Note: These are CFFI pointers, NOT python classes!)
    cairo_context = None
    pango_context = None

    @classmethod
    def create_pdf(
            cls,
            filename: str,
            width_in_mm: int,
            height_in_mm: int
    ) -> 'ContextCreator':
        """
        Generally used for acceptance tests

        :param filename:
            Where to put the pdf, relative to where the test is being executed.
        :param width_in_mm:
            The width of the PDF in millimeters
        :param height_in_mm:
            The height of the PDF in millimeters
        """
        cls.initialise_ffi()
        cc = ContextCreator()
        filename = filename.encode(sys.getfilesystemencoding())
        filename_pointer = cc.ffi.new('char[]', filename)

        # Convert millimeters to points.
        points_per_inch = 72
        mm_per_inch = 25.4
        points_per_mm = points_per_inch / mm_per_inch
        width_in_pts = width_in_mm * points_per_mm
        height_in_pts = height_in_mm * points_per_mm

        cc.cairo_surface = cc.cairo.cairo_pdf_surface_create(
            filename_pointer,
            width_in_pts,
            height_in_pts
        )
        cc.cairo_context = cc.cairo.cairo_create(cc.cairo_surface)
        cc.pango_context = cc._create_pango_context()
        return cc

    @classmethod
    def create_surface_without_output(cls) -> 'ContextCreator':
        """Generally used for functional tests where output is not checked"""
        cls.initialise_ffi()
        cc = ContextCreator()
        cc.ffi, cc.cairo, cc.pangocairo = cls.ffi, cls.cairo, cls.pangocairo
        cc.cairo_surface = cc.cairo.cairo_pdf_surface_create_for_stream(
            cc.ffi.NULL,
            cc.ffi.NULL,
            10,
            10
        )
        cc.cairo_context = cc.cairo.cairo_create(cc.cairo_surface)
        cc.pango_context = cc._create_pango_context()
        return cc

    @classmethod
    def initialise_ffi(cls):
        """
        Responsible to creating the Cairo and PangoCairo CFFIs. While we could
        use libraries like cairocffi and pangocairocffi directly, this might be
        problematic when managing dependencies. Therefore, we implement a small
        part of these libraries into this codebase.
        """
        if cls.ffi is not None:
            return

        cls.ffi = FFI()
        cls.ffi.include(ffi_builder)
        cls.ffi.cdef('''
            /* Cairo */
            typedef void cairo_t;
            typedef struct _cairo_surface cairo_surface_t;

            typedef enum _cairo_status {
                CAIRO_STATUS_SUCCESS = 0,

                CAIRO_STATUS_NO_MEMORY,
                CAIRO_STATUS_INVALID_RESTORE,
                CAIRO_STATUS_INVALID_POP_GROUP,
                CAIRO_STATUS_NO_CURRENT_POINT,
                CAIRO_STATUS_INVALID_MATRIX,
                CAIRO_STATUS_INVALID_STATUS,
                CAIRO_STATUS_NULL_POINTER,
                CAIRO_STATUS_INVALID_STRING,
                CAIRO_STATUS_INVALID_PATH_DATA,
                CAIRO_STATUS_READ_ERROR,
                CAIRO_STATUS_WRITE_ERROR,
                CAIRO_STATUS_SURFACE_FINISHED,
                CAIRO_STATUS_SURFACE_TYPE_MISMATCH,
                CAIRO_STATUS_PATTERN_TYPE_MISMATCH,
                CAIRO_STATUS_INVALID_CONTENT,
                CAIRO_STATUS_INVALID_FORMAT,
                CAIRO_STATUS_INVALID_VISUAL,
                CAIRO_STATUS_FILE_NOT_FOUND,
                CAIRO_STATUS_INVALID_DASH,
                CAIRO_STATUS_INVALID_DSC_COMMENT,
                CAIRO_STATUS_INVALID_INDEX,
                CAIRO_STATUS_CLIP_NOT_REPRESENTABLE,
                CAIRO_STATUS_TEMP_FILE_ERROR,
                CAIRO_STATUS_INVALID_STRIDE,
                CAIRO_STATUS_FONT_TYPE_MISMATCH,
                CAIRO_STATUS_USER_FONT_IMMUTABLE,
                CAIRO_STATUS_USER_FONT_ERROR,
                CAIRO_STATUS_NEGATIVE_COUNT,
                CAIRO_STATUS_INVALID_CLUSTERS,
                CAIRO_STATUS_INVALID_SLANT,
                CAIRO_STATUS_INVALID_WEIGHT,
                CAIRO_STATUS_INVALID_SIZE,
                CAIRO_STATUS_USER_FONT_NOT_IMPLEMENTED,
                CAIRO_STATUS_DEVICE_TYPE_MISMATCH,
                CAIRO_STATUS_DEVICE_ERROR,
                CAIRO_STATUS_INVALID_MESH_CONSTRUCTION,
                CAIRO_STATUS_DEVICE_FINISHED,
                CAIRO_STATUS_JBIG2_GLOBAL_MISSING,
                CAIRO_STATUS_PNG_ERROR,
                CAIRO_STATUS_FREETYPE_ERROR,
                CAIRO_STATUS_WIN32_GDI_ERROR,
                CAIRO_STATUS_TAG_ERROR,

                CAIRO_STATUS_LAST_STATUS
            } cairo_status_t;

            typedef cairo_status_t (*cairo_write_func_t) (
                void * closure,
                const unsigned char *data,
                unsigned int length
            );
            cairo_surface_t * cairo_pdf_surface_create_for_stream (
                cairo_write_func_t write_func,
                void *closure,
                double width_in_points,
                double height_in_points
            );
            void cairo_surface_destroy (cairo_surface_t *surface);
            cairo_t * cairo_create (cairo_surface_t *target);
            void cairo_surface_finish (cairo_surface_t *surface);
            void cairo_destroy (cairo_t *cr);

            cairo_surface_t * cairo_pdf_surface_create (
                const char *filename,
                double width_in_points,
                double height_in_points
            );
            void cairo_translate (cairo_t *cr, double tx, double ty);

            PangoContext * pango_cairo_create_context (cairo_t *cr);
            PangoLayout * pango_cairo_create_layout (cairo_t *cr);
            void pango_cairo_show_layout (cairo_t *cr, PangoLayout *layout);

            PangoFontMap * pango_cairo_font_map_new (void);
        ''')
        cls.ffi.set_source('pangocffi._generated.ffi', None)
        cls.cairo = _dlopen(
            cls.ffi,
            'cairo',
            'cairo-2',
            'cairo-gobject-2',
            'cairo.so.2')
        cls.pangocairo = _dlopen(
            cls.ffi,
            'pangocairo-1.0',
            'pangocairo-1.0-0'
        )

    def _create_pango_context(self):
        pango_context = self.pangocairo.pango_cairo_create_context(
            self.cairo_context
        )
        pango_context = pangocffi.ffi.cast('PangoContext *', pango_context)
        return pango_context

    def get_pango_context_as_class(self) -> Context:
        return Context.from_pointer(self.pango_context, gc=True)

    def close(self) -> None:
        if self.cairo_surface is not None:
            self.cairo.cairo_surface_finish(self.cairo_surface)
        self.pango_context = None
        self.cairo.cairo_destroy(self.cairo_context)
        self.cairo.cairo_surface_destroy(
            self.cairo_surface
        )
