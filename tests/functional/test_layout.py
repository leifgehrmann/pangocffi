from pangocffi import Context, Layout, Alignment


def test_layout_returns_identical_context():
    pass
    context = Context()
    layout = Layout(context)
    same_context = layout.get_context()
    assert same_context.get_pointer() == context.get_pointer()


def test_layout():
    pass
    context = Context()
    layout = Layout(context)

    layout.set_width(300)
    assert layout.get_width() == 300

    layout.set_height(400)
    assert layout.get_height() == 400

    layout.set_alignment(Alignment.CENTER)
    assert layout.get_alignment() is Alignment.CENTER

    ink_rect, logical_rect = layout.get_extents()
    assert logical_rect.width == 0
    assert logical_rect.height == 0

    # layout.set_markup(u'<span font="sans-serif 6">Παν語</span>')

    # ink_rect, logical_rect = layout.get_extents()
    # assert logical_rect.width == 0
    # assert logical_rect.height == 0
