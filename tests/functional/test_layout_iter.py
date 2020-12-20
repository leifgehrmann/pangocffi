from pangocffi import LayoutIter, ffi
import unittest


class TestLayoutIter(unittest.TestCase):

    def test_layout_iter_returns_null_from_null_pointer(self):
        with self.assertRaises(ValueError):
            LayoutIter.from_pointer(ffi.NULL)
