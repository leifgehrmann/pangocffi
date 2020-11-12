Changelog
---------

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

* Added new methods to ``Layout``
    * ``set_wrap``
    * ``get_wrap``

Version 0.6.0
.............

Released on 2020-09-17.

* Added new methods to ``Layout``
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
* Added new methods to ``Context``
    * ``set/get_base_gravity``
    * ``get_gravity``
    * ``set/get_gravity_hint``
* Added new methods to ``Layout``
    * ``get_text``
    * ``get_iter``
    * ``get_baseline``
    * ``get_line_count``
    * ``get/set_spacing``
* Added new method to ``Rectangle``
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
