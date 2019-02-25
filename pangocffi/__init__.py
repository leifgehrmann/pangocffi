"""
    pangocffi
    ~~~~~~~~~

    CFFI-based pango bindings for Python
    See README for details.

"""

from typing import Optional
import ctypes.util
from ._generated.ffi import ffi


def _dlopen(generated_ffi, *names):
    """Try various names for the same library, for different platforms."""
    for name in names:
        for lib_name in (name, 'lib' + name):
            try:
                path = ctypes.util.find_library(lib_name)
                lib = generated_ffi.dlopen(path or lib_name)
                if lib:
                    return lib
            except OSError:
                pass
    raise OSError("dlopen() failed to load a library: %s" % ' / '.join(names))


pango = _dlopen(ffi, 'pango', 'pango-1', 'pango-1.0')
gobject = _dlopen(ffi, 'gobject-2.0')


def pango_version() -> int:
    """Return the pango version number as a single integer,
    such as 14204 for ``1.42.4``.
    Major, minor and micro versions are "worth" 10000, 100 and 1 respectively.

    Can be useful as a guard for method not available in older pango versions::

        if pango_version() >= 11000:
            pango.pango_context.get_font_map(context)

    """
    return pango.pango_version()


def pango_version_string() -> str:
    """Return the pango version number as a string, such as ``1.42.4``."""
    return ffi.string(pango.pango_version_string()).decode('ascii')


def pango_version_check(
        required_major: int,
        required_minor: int,
        required_micro: int
) -> Optional[str]:
    """Return the pango version number as a string, such as ``1.42.4``."""
    check = pango.pango_version_check(
        required_major,
        required_minor,
        required_micro
    )

    if check == ffi.NULL:
        return None
    return ffi.string(check).decode('ascii')


# Imports are normally always put at the top of the file.
# But the wrapper API requires that the pango library be loaded first.
# Therefore, we have to disable linting rules for these lines.
from .enums import *  # noqa
from .convert import *  # noqa
from .font_description import FontDescription  # noqa
from .rectangle import Rectangle  # noqa
from .context import Context  # noqa
from .layout import Layout  # noqa
