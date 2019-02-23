from pangocffi import Context


def test_context_init_identical_context():
    context = Context()
    identical_context = Context.from_pointer(context.get_pointer())
    assert identical_context == context
