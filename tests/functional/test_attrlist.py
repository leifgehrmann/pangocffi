import copy
import unittest

from pangocffi import AttrList
from pangocffi.attributes import Attribute
from pangocffi.enums import Stretch


class TestLayout(unittest.TestCase):
    def test_init(self):
        a = AttrList()
        a.get_pointer()

    def test_from_pointer(self):
        a = AttrList()
        a.copy()
        b = AttrList.from_pointer(a.get_pointer())
        assert a == b

    def test_ref_and_unref(self):
        a = AttrList()
        a._ref()
        a._unref()

    def test_copy(self):
        a = AttrList()
        b = copy.copy(a)
        assert a == b
        c = copy.deepcopy(a)
        assert a == c

    def test_equal(self):
        a = AttrList()
        b = a.copy()
        assert a == b
        with self.assertRaises(NotImplementedError):
            a == 2

    def test_insert(self):
        a = AttrList()
        b = Attribute.from_size(5, 1, 4)
        a.insert(b)
        c = Attribute.from_foreground_alpha(6, 2, 4)
        a.insert_before(c)

    def test_change(self):
        a = AttrList()
        b = Attribute.from_size(5, 1, 6)
        a.change(b)

    def test_splice(self):
        # Idk how this works
        # copied from
        # https://gitlab.gnome.org/GNOME/pango/-/blob/master/tests/testattributes.c#L249
        base = AttrList()
        attr = Attribute.from_size(10, 0, -1)
        base.insert(attr)

        list = base.copy()
        other = AttrList()
        list.splice(other, 11, 5)

        list = base.copy()
        other = AttrList()
        attr = Attribute.from_size(20)
        attr.start_index = 0
        attr.end_index = 3
        other.insert(attr)
        attr1 = Attribute.from_stretch(Stretch.SEMI_CONDENSED)
        attr1.start_index = 2
        attr1.end_index = 4
        other.insert(attr1)

        list.splice(other, 11, 5)