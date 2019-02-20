pangocffi
=========

⚠️ This project is work-in-progress.

pangocffi is a `CFFI`_-based set of Python bindings for pango_.

The intention is to initially support operations for `cairo rendering`_ only and not to support Win32, Freetype, Xft and Coretext, but these could be added later.

Running tests
_____________

.. code-block::

   python setup.py test

.. _CFFI: https://cffi.readthedocs.org/
.. _pango: https://pango.org/
.. _cairo rendering: https://developer.gnome.org/pango/unstable/rendering.html
