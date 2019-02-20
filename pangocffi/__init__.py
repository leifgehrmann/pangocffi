"""
    pangocffi
    ~~~~~~~~~

    CFFI-based pango bindings for Python
    See README for details.

"""

import ctypes.util
from ._generated.ffi import ffi


def dlopen(ffi, *names):
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


pango = dlopen(ffi, 'pango', 'pango-1', 'pango-1.0')


def pango_version():
    """Return the pango version number as a single integer,
    such as 14204 for ``1.42.4``.
    Major, minor and micro versions are "worth" 10000, 100 and 1 respectively.

    Can be useful as a guard for method not available in older pango versions::

        if pango_version() >= 11000:
            pango.pango_context.get_font_map(context)

    """
    return pango.pango_version()


def pango_version_string():
    """Return the pango version number as a string, such as ``1.42.4``."""
    return ffi.string(pango.pango_version_string()).decode('ascii')
