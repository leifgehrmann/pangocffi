import os
import sys

from setuptools import setup


if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocffi does not support Python 2.x. Please use Python 3.'
    )

api_mode = False
if ('PANGOCFFI_API_MODE' in os.environ and
        int(os.environ['PANGOCFFI_API_MODE']) == 1):
    api_mode = True

setup(
    name='pangocffi',
    use_scm_version=True,
    install_requires=['cffi >= 1.1.0', 'cairocffi >= 1.7.2'],
    setup_requires=['cffi >= 1.1.0', 'cairocffi >= 1.7.2'],
    packages=['pangocffi'],
    cffi_modules=['pangocffi/ffi_build.py:ffi'] if api_mode else []
)

