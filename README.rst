pangocffi
=========

pangocffi is a `CFFI`_-based set of Python bindings for pango_.

See pangocairocffi_ for bindings that allow you to render pango objects with cairo.

pangocffi on its own is not that useful, since it depends on a PangoFontMap being declared against the PangoContext.
PangoFontMap instances can only be retrieved from libraries such as PangoCairo, PangoXft, PangoFT2, PangoWin32 (See gnome's documentation `Rendering with Pango`_ for a list of rendering engines).

The bindings are currently not fully implemented. Feel free to make a pull request to contribute! See :ref:`Binding Progress <binding-process>` for more information.

.. _CFFI: https://cffi.readthedocs.org/
.. _pango: https://pango.org/
.. _pangocairocffi: https://github.com/leifgehrmann/pangocairocffi
.. _Rendering with Pango: https://developer.gnome.org/pango/stable/rendering.html
