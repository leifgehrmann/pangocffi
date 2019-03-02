pangocffi on its own is not that useful, since it depends on a Pango
:class:`FontMap` being declared against the Pango :class:`Context`.
:class:`FontMap` instances can only be retrieved from libraries such as
PangoCairo, PangoXft, PangoFT2, PangoWin32 (See gnome's documentation
`Rendering with Pango`_ for a list of rendering engines).

See pangocairocffi_ for bindings that allow you to render pango objects with
cairo.

.. _pangocairocffi: https://github.com/leifgehrmann/pangocairocffi
.. _Rendering with Pango: https://developer.gnome.org/pango/stable/rendering.html
