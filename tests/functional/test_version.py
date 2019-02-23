import pangocffi


def test_pango_version():
    version_code = pangocffi.pango_version()
    assert isinstance(version_code, int)


def test_pango_version_string():
    version_code_string = pangocffi.pango_version_string()
    assert isinstance(version_code_string, str)


def test_pango_version_check():
    version_code_string = pangocffi.pango_version_check(1, 2, 3)
    assert version_code_string is None
    version_code_string = pangocffi.pango_version_check(0, 2, 3)
    assert isinstance(version_code_string, str)
