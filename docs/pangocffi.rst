pangocffi
=========

**Deprecation Notice:** pangocffi is no longer being maintained.
There are no plans to officially handover ownership of the project to another maintainer.
PyGObject can be used as a replacement, but will also require migrating from cairocffi to pycairo.
For more information, please see the :doc:`PyGObject Migration Guide <migration-guide>`.

pangocffi is a `CFFI`_-based set of Python bindings for pango_.

pangocffi on its own is not that useful, since it depends on a PangoFontMap
being declared against the PangoContext.
PangoFontMap instances can easily be retrieved from libraries such as
PangoCairo, PangoXft, PangoFT2, and PangoWin32 (See gnome's documentation
`'Rendering with Pango'`_ for a list of rendering engines).

See pangocairocffi_ for bindings that allow you to render pango objects with
cairo.

.. _pangocairocffi: https://github.com/leifgehrmann/pangocairocffi
.. _'Rendering with Pango': https://developer.gnome.org/pango/stable/rendering.html


The bindings are currently not fully implemented. Feel free to make a pull
request to contribute!

.. _CFFI: https://cffi.readthedocs.org/
.. _pango: https://pango.org/

Documentation
-------------

.. toctree::

    overview
    modules
    cffi-api
    binding-progress
    changelog
    contributing
    migration-guide
