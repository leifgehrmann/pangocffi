import pangocffi
from pangocffi import Layout, AttrList, Attribute, Underline, Rectangle, Style
from tests.context_creator import ContextCreator


def test_attributes():
    width = 150
    height = 50
    # CFFIs and Contexts
    context_creator = ContextCreator.create_pdf(
        'tests/acceptance/output/attributes.pdf', width, height
    )
    pangocairo = context_creator.pangocairo
    cairo_context = context_creator.cairo_context

    text = 'Hi from Παν語! This test is to make sure that text is correctly ' \
           'annotated, and to also highlight functionality that is not ' \
           'available from methods like pango.set_markup(\'...\'). ' \
           'For instance, Attribute.from_shape() allows you to embed a ' \
           'picture or a widget in a layout. Example: Ø.'
    text_utf8 = text.encode('utf-8')

    # Using pangocairocffi, this would be `pangocairocffi.create_layout()` with
    # a cairocffi context object.
    layout = Layout.from_pointer(
        pangocairo.pango_cairo_create_layout(cairo_context)
    )

    layout.set_width(pangocffi.units_from_double(width * 72 / 25.4))
    layout.set_text(text)

    attr_list = AttrList()

    # Example: Handling byte indexes correctly.
    # When handling byte indexes, make sure to always use UTF-8 byte strings.
    # For example , while the string '語' has a length of 1 character in
    # python, in a UTF-8 byte string this is 3 bytes: `0xe8 0xaa 0x9e`. Pango
    # will not like byte indexes that occur in the middle of a character.
    text_to_match = 'Παν語!'.encode('utf-8')
    match_index = text_utf8.index(text_to_match)
    match_index_end = match_index + len(text_to_match)
    attr_list.insert(Attribute.from_style(
        Style.ITALIC,
        match_index,
        match_index_end
    ))

    # Example: Color alpha
    # `set_markup()` doesn't appear to have the ability to control color
    # alphas, but it is supported by Attributes! Note that the alpha color for
    # underline and foreground text cannot be controlled separately.
    text_to_match = 'correctly'.encode('utf-8')
    match_index = text_utf8.index(text_to_match)
    match_index_end = match_index + len(text_to_match)
    attr_list.insert(Attribute.from_underline(
        Underline.ERROR, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_foreground_color(
        65535, 0, 0, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_underline_color(
        0, 0, 65535, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_background_color(
        0, 65535, 0, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_foreground_alpha(
        32768, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_background_alpha(
        8192, match_index, match_index_end
    ))

    # Example: Highlight multiple Monospace texts
    markup_texts = ('pango.set_markup(\'...\')', 'Attribute.from_shape()')
    for markup_text in markup_texts:
        text_to_match = markup_text.encode('utf-8')
        match_index = text_utf8.index(text_to_match)
        match_index_end = match_index + len(text_to_match)
        attr_list.insert(Attribute.from_family(
            'monospace',
            match_index,
            match_index_end
        ))

    # Example: Shape placeholders
    # `Attribute.from_shape()` can be used to insert a box within the layout.
    # In this case, we're inserting a 1cm square that sits on the baseline of
    # the final line. Note the negative y coordinate of the rectangle.
    # Visually, the background color will appear a bit larger, that's because
    # it will also apply a background below the baseline of the font.
    # Once rendered, it should be possible to retrieve the position of the
    # shape using using LayoutIter so that an actual image can be rendered in
    # place should you need to.
    text_to_match = 'Ø'.encode('utf-8')
    match_index = text_utf8.index(text_to_match)
    match_index_end = match_index + len(text_to_match)
    glyph_length = pangocffi.units_from_double(10 * 72 / 25.4)  # 10 mm
    ink = Rectangle(
        width=glyph_length, height=glyph_length, x=0, y=-glyph_length
    )
    logical = Rectangle(
        width=glyph_length, height=glyph_length, x=0, y=-glyph_length
    )
    attr_list.insert(Attribute.from_background_color(
        65535, 0, 0, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_background_alpha(
        8192, match_index, match_index_end
    ))
    attr_list.insert(Attribute.from_shape(
        ink,
        logical,
        match_index,
        match_index_end
    ))

    # Apply all the attributes to the layout
    layout.set_attributes(attr_list)

    # Using pangocairocffi, this would be `pangocairocffi.show_layout(layout)`
    pangocairo.pango_cairo_show_layout(cairo_context, layout.get_pointer())

    context_creator.close()
