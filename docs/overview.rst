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

Feel free to contribute a guide for how to install these dependencies on other
systems.

.. _homebrew: https://brew.sh

Installing pangocffi
____________________

Install with pip_::

    pip install pangocffi

.. _pip: https://pip.pypa.io/

Note: Python versions less than 3 are not supported.

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
