from pangocffi import Context, FontDescription


def test_context_init_identical_context():
    context = Context()
    identical_context = Context.from_pointer(context.get_pointer())
    assert identical_context == context


def test_context_properties():
    context = Context()

    desc = FontDescription()
    desc.set_family('sans-serif')
    context.set_font_description(desc)
    assert context.get_font_description().get_family() == 'sans-serif'
