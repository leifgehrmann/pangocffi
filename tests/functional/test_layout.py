from pangocffi import Context, FontDescription, Layout, Alignment


def test_layout_returns_identical_context():
    context = Context()
    layout = Layout(context)
    same_context = layout.get_context()
    assert same_context.get_pointer() == context.get_pointer()


def test_layout_properties():
    context = Context()
    layout = Layout(context)

    desc = FontDescription()
    desc.set_family('sans-serif')
    layout.set_font_description(desc)
    same_desc = layout.get_font_description()
    assert same_desc.get_family() == desc.get_family()

    desc.set_family('serif')
    assert same_desc.get_family() != desc.get_family()

    layout.set_width(300)
    assert layout.get_width() == 300

    layout.set_height(400)
    assert layout.get_height() == 400

    layout.set_alignment(Alignment.CENTER)
    assert layout.get_alignment() is Alignment.CENTER

    ink_rect, logical_rect = layout.get_extents()
    assert logical_rect.width == 0
    assert logical_rect.height == 0

    width, height = layout.get_size()
    assert width == 0
    assert height == 0

    # layout.set_text('hello')
    # layout.set_markup(u'<span font="sans-serif 6">test</span>')

    width, height = layout.get_size()
    assert width == 0
    assert height == 0

    # ink_rect, logical_rect = layout.get_extents()
    # assert logical_rect.width == 0
    # assert logical_rect.height == 0
