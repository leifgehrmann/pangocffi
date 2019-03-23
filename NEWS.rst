Changelog
---------

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
