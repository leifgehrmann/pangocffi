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

Matrix
______

Glyph String
____________

Glyph Item
__________

Fonts
=====

Structures representing abstract fonts.

Font Description
________________

.. autoclass:: FontDescription

Font Metrics
____________

Font Map
________

Font Set
________

Font Fields
___________

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

Tab Stops
=========

Structures for storing tab stops.

Text Attribute Markup
=====================

See https://developer.gnome.org/pango/stable/PangoMarkupFormat.html for details
on how to use the Pango Text Attribute Markup Language.

Layout Objects
==============

High-level layout driver objects.

Layout
______

.. autoclass:: Layout

Layout Line
___________

Layout Modes
____________

Wrap Mode
---------
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

Language
________

Bidirectional Text
==================

Types and functions to help with handling bidirectional text.

Vertical Text
=============

Laying text out in vertical directions.
