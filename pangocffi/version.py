from . import pango, ffi


def get_pango_version() -> str:
    """Return the pango version number as a string, such as ``1.42.4``."""
    return ffi.string(pango.pango_version_string()).decode('ascii')
