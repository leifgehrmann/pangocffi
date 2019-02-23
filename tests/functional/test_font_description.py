from pangocffi import FontDescription
from pangocffi import Gravity, Stretch, Style, Variant, Weight


def test_font_description_init_identical():
    desc = FontDescription()
    identical_desc = desc.from_pointer(desc.get_pointer())
    assert identical_desc == desc


def test_setting_properties():
    desc = FontDescription()

    desc.set_family('sans-serif')
    assert desc.get_family() == 'sans-serif'

    desc.set_style(Style.NORMAL)
    assert desc.get_style() == Style.NORMAL

    desc.set_variant(Variant.NORMAL)
    assert desc.get_variant() == Variant.NORMAL

    desc.set_weight(Weight.BOOK)
    assert desc.get_weight() == Weight.BOOK

    desc.set_stretch(Stretch.NORMAL)
    assert desc.get_stretch() == Stretch.NORMAL

    desc.set_size(123)
    assert desc.get_size() == 123
    assert not desc.get_size_is_absolute()

    desc.set_absolute_size(1.23)
    assert desc.get_size() != 123
    assert desc.get_size_is_absolute()

    desc.set_gravity(Gravity.EAST)
    assert desc.get_gravity() == Gravity.EAST
