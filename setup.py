import sys
import setuptools
from pathlib import Path

if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocffi does not support Python 2.x. Please use Python 3.'
    )

version = (Path(__file__).parent / 'pangocffi' / 'VERSION').read_text().strip()
long_description = (Path(__file__).parent / 'README.rst').read_text().strip()

setuptools.setup(
    version=version,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=setuptools.find_packages(),
    setup_requires=['pytest-runner'],
    cffi_modules=[
        'pangocffi/ffi_build.py:ffi'
    ]
)
