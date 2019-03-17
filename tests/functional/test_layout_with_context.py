from pangocffi import Layout
from .context_creator import create_pango_context
import unittest


class TestLayoutWithContext(unittest.TestCase):

    @staticmethod
    def test_layout_setting_text():
        layout = Layout(create_pango_context())

        layout.set_text('Hi from Παν語')
        assert layout.get_text() == 'Hi from Παν語'

        layout.set_markup('<span font="italic 30">Hello from Παν語</span>')
        assert layout.get_text() == 'Hello from Παν語'
