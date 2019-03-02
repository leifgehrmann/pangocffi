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
cdefs_file = open(Path(__file__).parent / 'cdefs.txt', 'r')
cdefs = cdefs_file.read()

# cffi definitions, in the order outlined in:
# https://developer.gnome.org/pango/stable
ffi = FFI()
ffi.set_source('pangocffi._generated.ffi', None)
ffi.cdef("""
    typedef ... GType;
    typedef unsigned int guint8;
    typedef unsigned int guint16;
    typedef unsigned int guint32;
    typedef unsigned int guint;
    typedef int gint;
    typedef int gint32;
    typedef gint gboolean;
    typedef char gchar;
    typedef unsigned char guchar;
    typedef ... gunichar;
    typedef void* gpointer;
    typedef ... gconstpointer;
    typedef ... GObject;
    typedef ... GObjectClass;
    typedef ... GString;
    typedef ... GDestroyNotify;
    typedef ... GList;
    typedef ... GSList;
    typedef ... GError;
    typedef ... GMarkupParseContext;
    typedef ... GTypeModule;
    
    void g_object_unref (gpointer object);
""")
ffi.cdef(cdefs)

if __name__ == '__main__':
    ffi.compile()
