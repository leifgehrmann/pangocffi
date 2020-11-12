pangocffi
=========

.. image:: https://img.shields.io/pypi/v/pangocffi.svg
    :target: https://pypi.python.org/pypi/pangocffi
    :alt: Latest PyPi Release

.. image:: https://img.shields.io/pypi/pyversions/pangocffi.svg?style=flat
    :target: https://pypi.python.org/pypi/pangocffi
    :alt: Supported Python Versions

.. image:: https://github.com/leifgehrmann/pangocffi/workflows/Build/badge.svg?branch=master
    :target: https://github.com/leifgehrmann/pangocffi/actions

.. image:: https://readthedocs.org/projects/pangocffi/badge/?version=latest
    :target: https://pangocffi.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://codecov.io/gh/leifgehrmann/pangocffi/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/leifgehrmann/pangocffi
    :alt: Code Coverage

pangocffi is a `CFFI`_-based set of Python bindings for pango_.

pangocffi on its own is not that useful, since it depends on a PangoFontMap
being declared against the PangoContext.
PangoFontMap instances can easily be retrieved from libraries such as
PangoCairo, PangoXft, PangoFT2, and PangoWin32 (See gnome's documentation
`Rendering with Pango`_ for a list of rendering engines).

See pangocairocffi_ for bindings that allow you to render pango objects with
cairo.

.. _pangocairocffi: https://github.com/leifgehrmann/pangocairocffi
.. _Rendering with Pango: https://developer.gnome.org/pango/stable/rendering.html


The bindings are currently not fully implemented. Feel free to make a pull
request to contribute!

.. _CFFI: https://cffi.readthedocs.org/
.. _pango: https://pango.org/
