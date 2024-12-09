import os
import sys

from setuptools import setup


if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocffi does not support Python 2.x. Please use Python 3.'
    )

setup(
    name='pangocffi',
    use_scm_version=True,
    install_requires=['cffi >= 1.1.0'],
    setup_requires=['cffi >= 1.1.0'],
    packages=['pangocffi'],
    cffi_modules=['pangocffi/ffi_build.py:build_ffi']
)

