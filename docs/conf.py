from pathlib import Path
import sys
import os

from unittest.mock import MagicMock, Mock

generated_file = Path(__file__).parent.parent / "pangocffi/_generated/ffi.py"
if not os.path.exists(generated_file):

    class AttrMock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
            if name in ["_mock_methods", "__qualname__", "__args__"]:
                # noinspection PyUnresolvedReferences
                return super.__getattr__(cls, name)
            else:
                mm = AttrMock()
            mm.__repr__ = lambda s: ("pangocffi.ffi." + name)
            mm.__str__ = Mock(return_value=("pangocffi.ffi." + name))
            return mm

    class ModuleMock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
            mm = AttrMock()
            return mm

    MOCK_MODULES = ["pangocffi._generated", "pangocffi._generated.ffi"]
    sys.modules.update((mod_name, ModuleMock()) for mod_name in MOCK_MODULES)


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
]
master_doc = "index"
project = "pangocffi"
copyright = "2019, Leif Gehrmann"
release = (Path(__file__).parent.parent / "pangocffi" / "VERSION")
release = release.read_text().strip()
version = ".".join(release.split(".")[:2])
exclude_patterns = ["_build"]
autodoc_member_order = "bysource"
autodoc_default_flags = ["members"]
intersphinx_mapping = {
    "http://docs.python.org/": None,
    "https://pycairo.readthedocs.io/en/latest/": None,
}

sys.path.insert(0, os.path.abspath(".."))

html_theme = "sphinx_rtd_theme"
