import sys
import distutils.errors
import setuptools

if sys.version_info.major < 3:
    raise RuntimeError(
        'pangocffi does not support Python 2.x. Please use Python 3.'
    )

"""
Raise error if one attempts to build pangocffi as `bdist_wheel`. This is
necessary when `wheel` is installed in the environment, because pip will
automatically attempt to cache the package using `bdist_wheel`. By raising an
error pip will fallback to installing as `sdist`.
See: https://stackoverflow.com/questions/58289062/prevent-pip-from-caching-a-package
"""
bdist_wheel = None
try:
    import wheel.bdist_wheel

    class bdist_wheel(wheel.bdist_wheel.bdist_wheel):
        def run(self, *args, **kwargs):
            raise distutils.errors.DistutilsClassError(
                'pangocffi does not support bdist_wheel. Please use sdist.'
            )
except ModuleNotFoundError:
    pass

setuptools.setup(
    setup_requires=['pytest-runner'],
    cffi_modules=[
        'pangocffi/ffi_build.py:ffi'
    ],
    cmdclass={'bdist_wheel': bdist_wheel}
)
