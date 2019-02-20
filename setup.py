import sys
from setuptools import setup

if sys.version_info.major < 3:
    raise RuntimeError('pangocffi does not support Python 2.x. Please use Python 3.')

setup(
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    cffi_modules=[
        'pangocffi/ffi_build.py:ffi'
    ]
)
