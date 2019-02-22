pangocffi
=========

⚠️ This project is work-in-progress.

pangocffi is a `CFFI`_-based set of Python bindings for pango_.

Usage
_____

Assuming Pango has been installed, and running Python v3:

.. code-block::

   from pangocffi import Context, Layout, Alignment, Rectangle
   context = Context()
   layout = Layout(context)
   layout.set_width(300)
   layout.set_alignment(Alignment.CENTER)
   layout.set_markup(u"Παν語")

   (ink_rect, logical_rect) = layout.get_extents()

   print(ink_rect.width)
   print(ink_rect.height)

Running tests
_____________

.. code-block::

   python setup.py test

.. _CFFI: https://cffi.readthedocs.org/
.. _pango: https://pango.org/
.. _cairo rendering: https://developer.gnome.org/pango/unstable/rendering.html
