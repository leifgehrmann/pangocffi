from pangocffi import Context, Layout, Alignment


def test_layout_returns_identical_context():
    context = Context()
    layout = Layout(context)
    same_context = layout.get_context()
    assert isinstance(same_context, Context)
    assert same_context.get_pointer() == context.get_pointer()


def test_layout():
    context = Context()
    layout = Layout(context)

    layout.set_width(300)
    assert layout.get_width() == 300

    layout.set_height(300)
    assert layout.get_height() == 300

    layout.set_alignment(Alignment.CENTER)
    assert layout.get_alignment() is Alignment.CENTER
