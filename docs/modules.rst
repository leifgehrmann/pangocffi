Python API reference
####################

.. module:: pangocffi

Rendering
=========

Functions to run the rendering pipeline.

.. autoclass:: Context

Glyph Storage
=============

Structures for storing information about glyphs.

Units and conversion
____________________

.. autofunction:: pangocffi.units_to_double

.. autofunction:: pangocffi.units_from_double

Matrix
______

API not implemented yet.

Glyph String
____________

API not implemented yet.

Glyph Item
__________

API not implemented yet.

Fonts
=====

Structures representing abstract fonts.

Font Description
________________

.. autoclass:: FontDescription

Font Metrics
____________

API not implemented yet.

Font Map
________

API not implemented yet.

Font Set
________

API not implemented yet.

Font Fields
___________

API not implemented yet.

Style
-----
.. autoclass:: Style

Weight
------
.. autoclass:: Weight

Variant
-------
.. autoclass:: Variant

Stretch
-------
.. autoclass:: Stretch

FontMask
--------
.. autoclass:: FontMask

Text Attributes
===============

Font and other attributes for annotating text.

API not implemented yet.

Tab Stops
=========

Structures for storing tab stops.

API not implemented yet.

Text Attribute Markup
=====================

See `Gnome's documentation`_ for details on how to use the Pango Text Attribute
Markup Language.

.. _`Gnome's documentation`: https://developer.gnome.org/pango/stable/PangoMarkupFormat.html

Layout Objects
==============

High-level layout driver objects.

Layout
______

.. autoclass:: Layout

Layout Line
___________

API not implemented yet.

Layout Modes
____________

API not implemented yet.

Wrap Mode
---------

API not implemented yet.

Ellipsize Mode
--------------
.. autoclass:: EllipsizeMode

Alignment
---------
.. autoclass:: Alignment

Scripts and Languages
=====================

Identifying writing systems and languages.

Script
______

API not implemented yet.

Language
________

API not implemented yet.

Bidirectional Text
==================

Types and functions to help with handling bidirectional text.

API not implemented yet.

Vertical Text
=============

Laying text out in vertical directions.

Gravity
_______

.. autoclass:: Gravity

Gravity Hints
_____________

.. autoclass:: GravityHint

Low Level Functionality
=======================

Version Checking
________________

.. autofunction:: pangocffi.pango_version

.. autofunction:: pangocffi.pango_version_string