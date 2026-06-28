.. _migration-guide:

PyGObject Migration Guide
=========================

pangocffi (and pangocairocffi) can be replaced by PyGObject_, but there are several dependencies and API calls that need to be changed.
The migration is worthwhile because PyGObject's bindings are more complete than pangocffi's, and it's also maintained by more people.
However there are a few drawbacks, like needing to replace cairocffi with Pycairo, which not everyone will be able to do.

pangocffi can continue to be used in the short term, but if it breaks in future versions of Python, cairocffi, and cffi, the project will have to be forked and fixed.
In such an event, the LGPL 2.1 license must be respected.

This guide covers various details for switching to PyGObject, including:

* Replacing system dependencies
* Replacing Python packages
* Replacing usages of cairocffi with Pycairo_
* Switching usages of pangocffi and pangocairocffi's API to PyGObject
* An example using PyGObject

.. _PyGObject: https://pygobject.gnome.org/

.. _Pycairo: https://pycairo.readthedocs.io/

Replacing System Dependencies
_____________________________

Which system dependencies to install will differ between Linux, macOS, Windows, etc.

To give some general guidance, here's a before and after of the system dependencies specifically for **Debian Trixie**. Other systems might have different names for these dependencies.

Before the migration, pangocffi and pangocairocffi required these dependencies:

* ``libcairo2``
* ``libpango-1.0-0``
* ``libpangocairo-1.0-0``

To use Pango and PangoCairo with PyGObject, install these dependencies:

* ``pkg-config``
* ``libcairo2-dev``
* ``libpango1.0-dev``
* ``libpangocairo-1.0-0``
* ``libgirepository-2.0-dev``

The ``-dev`` suffix is important because these will include bindings that PyGObject will use to interface with Pango and PangoCairo.

If the libraries above don't work, see `Getting Started with Pycairo`_ and `Getting Started with PyGObject`_ for guidance on which additional libraries to install.
Note that PyGObject's guide might include extra dependencies that are irrelevant for using Pango and Pangocairo.

.. _Getting Started with Pycairo: https://pycairo.readthedocs.io/en/latest/getting_started.html

.. _Getting Started with PyGObject: https://pygobject.gnome.org/getting_started.html

Replacing Python Packages
_________________________

Before the migration, these were the Python packages necessary::

    pip install cairocffi
    pip install pangocffi
    pip install pangocairocffi

After the migration, these are now packages to install instead::

    pip install pycairo
    pip install pygobject
    pip install pygobject-stubs # Optional for type-hinting

Switching from cairocffi to Pycairo
___________________________________

cairocffi does not appear to work with PyGObject, but Pycairo does. Therefore cairocffi must be replaced with Pycairo.

cairocffi is meant to be a drop-in replacement for Pycairo, so it should be a matter of changing the import in a lot of places from one package to another::

    # Before
    import cairocffi as cairo
    from cairocffi import ImageSurface

    # After
    import cairo
    from cairo import ImageSurface

Type hinting also changes subtly::

    # Before
    my_function(
        surface: cairo.surfaces.Surface,
        context: cairo.context.Context
    ) -> None

    # After
    my_function(
        surface: cairo.Surface,
        context: cairo.Context
    ) -> None

There are some inconsistencies between cairocffi and PyCairo, so make sure to review the code for errors. For example, in Pycairo, matrices cannot be copied using ``.copy()``::

    # Before, cairocffi.Matrix has a copy method
    new_matrix = old_matrix.copy()

    # After, Pycairo requires an explicit initialisation of a new Matrix
    new_matrix = cairo.Matrix(
        old_matrix.xx,
        old_matrix.yx,
        old_matrix.xy,
        old_matrix.yy,
        old_matrix.x0,
        old_matrix.y0,
    )

Switching from pangocffi and pangocairocffi's API to PyGObject
______________________________________________________________

There are a few differences between pangocffi's and PyGObject's implementation of API methods.
Below are a few examples:

Imports
^^^^^^^

pangocffi was imported with::

    import pangocffi
    import pangocairocffi

PyGObject instead requires::

    import gi
    gi.require_version("Pango", "1.0")
    gi.require_version("PangoCairo", "1.0")
    from gi.repository import Pango  # noqa: E402
    from gi.repository import PangoCairo  # noqa: E402

Getters and setters
^^^^^^^^^^^^^^^^^^^

pangocffi uses the ``property`` decorator pattern for implementing getter and setter methods::

    my_width = layout.width
    layout.width = 123

PyGObject however uses plain ``get_x`` and ``set_x`` for getter and setter methods::

    my_width = layout.get_width()
    layout.set_width(123)

Using Layout Markup
^^^^^^^^^^^^^^^^^^^

pangocffi's Layout object has a method called ``apply_markup(...)``.
PyGObject calls the method ``set_markup(...)`` instead.

PyGObject API reference
^^^^^^^^^^^^^^^^^^^^^^^

There are likely many more differences not listed here.
See the GNOME Python API for Pango_ and PangoCairo_ for more details on additional methods.
For other GNOME libraries, see the `GNOME Python API documentation`_.

.. _Pango: https://api.pygobject.gnome.org/Pango-1.0/index.html
.. _PangoCairo: https://api.pygobject.gnome.org/PangoCairo-1.0/index.html
.. _GNOME Python API documentation: https://api.pygobject.gnome.org

Example
_______

In case there are any installation issues, a `functioning example`_ has been created to use as a reference.
The example runs in a in a Debian environment using Docker_.
This can be useful for troubleshooting any unexpected migration issues when switching from pangocffi to PyGObject.

.. _functioning example: https://codeberg.org/leifgehrmann/pango-python-test
.. _Docker: https://docs.docker.com/get-started/
