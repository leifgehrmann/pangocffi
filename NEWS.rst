Changelog
---------

Version 0.10.0
..............

Released on 2020-12-30.

* All ``from_pointer()`` methods in pangocffi by default will not apply a
  garbage collection callback. **If you are using pangocairocffi, you will need
  to update to the latest version (v0.6.0) to avoid any potential issues.**
  This change is done mainly for consistency. If the original functionality is
  desired, adding ``gc=True`` should be enough (In other words,
  ``from_pointer(pointer, gc=True)``). This affects the following methods:

    * ``Context.from_pointer()``
    * ``Layout.from_pointer()``

* Fixed an issue with ``Attribute`` in an ``AttrList`` causing segmentation
  faults when the list was being copied because the attribute was improperly
  being garbage collected. This was solved by simply removing the call to
  ``ffi.gc(pointer, pango.pango_attribute_destroy)``. If there are any issues
  with this change, please raise an issue in the issue tracker.

* Fixed a mistake with ``Attribute`` where the ``end_index`` was incorrectly
  being set against the ``start_index``.

* Added setter methods for the properties of ``Rectangle`` and adds arguments
  to ``__init__()`` for setting the properties individually.

Version 0.9.0
.............

Released on 2020-12-19.

* pangocffi now depends on GLib 2.0. It's very likely GLib is already installed
  since pangocffi already depended on GObject, but if not, pangocffi will raise
  an error on import.

* Added the following new classes

    * ``Attribute``
    * ``AttrList``
    * ``Color``

* Added new methods to ``Layout``

    * ``set_attributes``
    * ``get_attributes``

* Added new enum ``Underline``.

* Fixed issue with ``Context.get_gravity_hint`` calling the wrong pango
  function.

* Added the ability to configure loading a specific library via the following
  environment variables:

    * ``PANGO_LOCATION``
    * ``GLIB_LOCATION``
    * ``GOBJECT_LOCATION``

Version 0.8.0
.............

Released on 2020-11-13.

* C-FFI bindings are now generated at runtime, rather than at installation.
  This was done to avoid common installation issues like
  ``ModuleNotFoundError: No module named 'pangocffi._generated'``. This change
  does mean the bindings are re-compiled the first time ``import pangocffi`` is
  called in a python session, but it takes less than a second to do this. If
  there are any issues with this change, please raise an issue in the issue
  tracker.
* Because of the aforementioned change, modules that depend on pangocffi's
  bindings being generated upon installation rather than at runtime, like
  pangocairocffi, will break. Either lock your version of pangocffi to 0.7.0
  or upgrade the module to the latest version which is compatible with 0.8.0 of
  pangocffi.
* Support for Python 3.5 has been dropped because it has reached end-of-life.

Version 0.7.0
.............

Released on 2020-10-17.

* Added new methods to ``Layout``:

    * ``set_wrap``
    * ``get_wrap``

Version 0.6.0
.............

Released on 2020-09-17.

* Added new methods to ``Layout``:

    * ``set_ellipsize``
    * ``get_ellipsize``

Version 0.5.0
.............

Released on 2019-10-08.

* Extended library names to include current Win64 library names.

Version 0.4.0
.............

Released on 2019-03-23.

* Added ``FFIInstanceBuilder`` to separate C FFI build logic from the actual
  C FFI builder.

Version 0.3.0
.............

Released on 2019-03-17.

* Added the following new classes:

    * ``GlyphItem``
    * ``GlyphItemIter``
    * ``Item``
    * ``LayoutIter``
    * ``LayoutRun``

* Added new methods to ``Context``:

    * ``set/get_base_gravity``
    * ``get_gravity``
    * ``set/get_gravity_hint``

* Added new methods to ``Layout``:

    * ``get_text``
    * ``get_iter``
    * ``get_baseline``
    * ``get_line_count``
    * ``get/set_spacing``

* Added new method to ``Rectangle``:

    * ``get_pointer``

* Corrected return types (``ffi.CData`` was previously ``ctypes.c_void_p``)

Version 0.2.0
.............

Released on 2019-03-09.

* ``FontDescription.getWeight()`` now returns ``int``, instead of the
  ``Weight`` enum.
* Improved test coverage.

Version 0.1.1
.............

Released on 2019-03-06.

* Fixed installation issue for Python 3.5.
* Added Tox config that tests a fresh install of pangocffi when testing
  between versions of python.

Version 0.1.0
.............

Released on 2019-03-03.

* Added support for Python 3.5 and 3.6 (previously only 3.7 was supported)
* Added config file for tox to test pangocffi for python versions 3.5, 3.6, and
  3.7

Version 0.0.1
.............

Released on 2019-03-02.

First PyPI release.
