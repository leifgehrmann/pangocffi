import sys
import setuptools

if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocffi does not support Python 2.x. Please use Python 3.'
    )

setuptools.setup(
    setup_requires=['pytest-runner'],
    cffi_modules=[
        'pangocffi/ffi_build.py:ffi'
    ]
)
