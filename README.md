# pangocffi

[![Latest PyPi Release](https://img.shields.io/pypi/v/pangocffi.svg)](https://pypi.python.org/pypi/pangocffi)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pangocffi.svg?style=flat)](https://pypi.python.org/pypi/pangocffi)
[![Build Status](https://github.com/leifgehrmann/pangocffi/actions/workflows/build.yml/badge.svg)](https://github.com/leifgehrmann/pangocffi/actions)
[![Documentation Status](https://readthedocs.org/projects/pangocffi/badge/?version=latest)](https://pangocffi.readthedocs.io/en/latest/?badge=latest)
[![Code Coverage](https://codecov.io/gh/leifgehrmann/pangocffi/branch/master/graph/badge.svg)](https://codecov.io/gh/leifgehrmann/pangocffi)

pangocffi is a [CFFI]-based set of Python bindings for [pango].

pangocffi on its own is not that useful, since it depends on a PangoFontMap
being declared against the PangoContext.
PangoFontMap instances can easily be retrieved from libraries such as
PangoCairo, PangoXft, PangoFT2, and PangoWin32 (See gnome's documentation
['Rendering with Pango'] for a list of rendering engines).

See [pangocairocffi] for bindings that allow you to render pango objects with
cairo.

[pangocairocffi]: https://github.com/leifgehrmann/pangocairocffi
['Rendering with Pango']: https://developer.gnome.org/pango/stable/rendering.html


The bindings are currently not fully implemented. Feel free to make a pull
request to contribute!

[CFFI]: https://cffi.readthedocs.org/
[pango]: https://pango.org/

## Installation and usage

See ['Overview'] for information on how to install the necessary libraries.

See ['Python API Reference'] for additional information on all the objects.

['Overview']: https://pangocffi.readthedocs.io/en/latest/overview.html
['Python API Reference']: https://pangocffi.readthedocs.io/en/latest/modules.html

## Contributing

If you would like to contribute to this project, either by leaving feedback or
submitting a pull request, please read '[CONTRIBUTING.md]'.

[CONTRIBUTING.md]: CONTRIBUTING.md
