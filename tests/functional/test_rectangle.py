from pangocffi import Rectangle


def test_rectangle_properties():
    rect = Rectangle()
    rect.x = 100
    rect.y = 200
    rect.width = 300
    rect.height = 400
    assert rect.x == 100
    assert rect.y == 200
    assert rect.width == 300
    assert rect.height == 400


def test_rectangle_init_with_no_values():
    rect = Rectangle()
    assert rect.x == 0
    assert rect.y == 0
    assert rect.width == 0
    assert rect.height == 0


def test_rectangle_init_with_values():
    rect = Rectangle(x=100, y=200, width=300, height=400)
    assert rect.x == 100
    assert rect.y == 200
    assert rect.width == 300
    assert rect.height == 400


def test_rectangle_pointers():
    rect = Rectangle()
    same_rect = rect.from_pointer(rect.pointer)
    assert same_rect.x == 0
