Overview
========

**Deprecation Notice:** pangocffi is no longer being maintained.
There are no plans to officially handover ownership of the project to another maintainer.
PyGObject can be used as a replacement, but will also require migrating from cairocffi to pycairo.
For more information, please see the :doc:`PyGObject Migration Guide <migration-guide>`.

Installing
----------

Installing Pango, GLib, FFI
______________________________

pangocffi depends on Pango_, GLib_, and libffi_ being installed.

.. _Pango: https://www.pango.org/Download
.. _GLib: https://wiki.gnome.org/Projects/GLib
.. _libffi: https://sourceware.org/libffi/

Feel free to contribute a guide for how to install these dependencies on other
systems.

Linux
^^^^^

For Ubuntu/Debian::

    apt install libffi-dev libpango-1.0-0
    # To use pangocffi (and pangocairocffi) with cairo
    apt install libcairo2 libpangocairo-1.0-0

Other Linux distributions may require a different setup.

macOS
^^^^^

Use `homebrew`_ to install the packages::

    brew install pkg-config
    brew install libffi
    brew install pango
    brew install glib

.. _homebrew: https://brew.sh

Windows
^^^^^^^

If you are using a 64-bit Python, you can use `this binary installer`_ to install GTK 3.
Use ``python --version --version`` to check whether you're running 32-bit or 64-bit Python.

.. _`this binary installer`: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

Installing pangocffi
____________________

Install with pip_::

    pip install pangocffi

.. _pip: https://pip.pypa.io/

Note: Python versions < 3.10 are not supported.

Importing pangocffi
-------------------

The module to import is named ``pangocffi``, however you are welcome to alias
the module as ``pango``::

    import pangocffi as pango

pangocffi will dynamically load Pango, GLib, and GObject as a shared library
upon importing. If it fails to find it, you will see an exception like this::

    OSError: dlopen() failed to load pango: pango / pango-1 / ...

If Pango, GLib, or GObject are not installed as a shared library, pangocffi
supports specifying a path via environment variables respectively:
``PANGO_LOCATION``, ``GLIB_LOCATION``, ``GOBJECT_LOCATION``.

Basic usage
-----------

.. include:: rendering-pango.rst
