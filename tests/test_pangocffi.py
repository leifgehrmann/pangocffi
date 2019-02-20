import pangocffi

def test_version():
    version_code = pangocffi.pango_version()
    assert isinstance(version_code, int)

def test_version_string():
    version_code_string = pangocffi.pango_version_string()
    assert isinstance(version_code_string, str)
