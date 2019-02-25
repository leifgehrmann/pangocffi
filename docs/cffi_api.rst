CFFI API
========

.. currentmodule:: pangocffi

pangocffi’s :doc:`API <api>` is made of a number of
:ref:`wrapper <wrappers>` classes
that provide a more Pythonic interface for various pango objects.
Functions that take a pointer as their first argument become methods,
error statuses become exceptions,
and :ref:`reference counting <refcounting>` is hidden away.

In order to use other C libraries that use integrate with pango,
or if pangocffi’s API is not sufficient
you can access cairo’s lower level C pointers and API through CFFI_.

.. _CFFI: https://cffi.readthedocs.org/


Module-level objects
--------------------

.. data:: ffi

    A :class:`cffi.FFI` instance with all of the pango C API declared.

.. data:: pango

    The libpango library, pre-loaded with :meth:`ffi.dlopen`.
    All cairo functions are accessible as attributes of this object::

        import pangocffi
        from pangocffi import pango as pango_c, SURFACE_TYPE_XLIB

        if pango_c.pango_renderer_draw_layout(my_renderer, layout.get_pointer(), 0, 0):
            ...

    See the `cairo manual`_ for details.

    .. _cairo manual: http://cairographics.org/manual/
