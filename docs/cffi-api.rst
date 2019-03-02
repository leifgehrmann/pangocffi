CFFI API
========

.. currentmodule:: pangocffi

pangocffi’s :doc:`API <modules>` is made of a number of wrapper classes
that provide a more Pythonic interface for various pango objects.
Functions that take a pointer as their first argument become methods.

In order to use other C libraries that integrate with pango,
or if pangocffi’s API is not sufficient,
you can access pango’s lower level C pointers and API through CFFI_.

.. _CFFI: https://cffi.readthedocs.org/

Module-level objects
--------------------

.. data:: ffi

    A :class:`cffi.FFI` instance with all of the pango C API declared.

.. data:: pango

    The libpango library, pre-loaded with :meth:`ffi.dlopen`.
    All pango functions are accessible as attributes of this object::

        from pangocffi import Context, Layout
        from pangocffi import pango as pango_c

        context = Context()
        layout = Layout(context)

        pango_c.pango_renderer_draw_layout(..., layout.get_pointer(), 0, 0)

    See the `pango reference manual`_ for details.

.. _pango reference manual: https://developer.gnome.org/pango/stable/index.html
