Overview
========

Installing
----------

Installing Pango, GLib, FFI
______________________________

pangocffi depends on Pango_, GLib_, and libffi_ being installed.

.. _Pango: https://www.pango.org/Download
.. _GLib: https://wiki.gnome.org/Projects/GLib
.. _libffi: https://sourceware.org/libffi/

* On Mac OS, this is as easy as installing `homebrew`_ and then running::

    brew install pkg-config
    brew install libffi
    brew install pango
    brew install glib

* On Linux, these packages are usually installed as part of the base OS.

* On Windows, if you are using a 64-bit Python, you can use `this binary installer`_ to install GTK 3. Use ``python --version --version`` to check whether you're running 32-bit or 64-bit Python.

.. _homebrew: https://brew.sh
.. _`this binary installer`: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

Feel free to contribute a guide for how to install these dependencies on other
systems.

Installing pangocffi
____________________

Install with pip_::

    pip install pangocffi

.. _pip: https://pip.pypa.io/

Note: Python versions < 3.5 are not supported.

Importing pangocffi
-------------------

The module to import is named ``pangocffi``, however you are welcome to alias
the module as ``pango``::

    import pangocffi as pango

pangocffi will dynamically load Pango as a shared library upon importing.
If it fails to find it, you will see an exception like this::

    OSError: library not found: 'pango'


Basic usage
-----------

.. include:: rendering-pango.rst
