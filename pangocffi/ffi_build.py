"""
    pangocffi.ffi_build
    ~~~~~~~~~~~~~~~~~~~

    Build the cffi bindings for pangocffi

"""

import importlib.util
import os
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent))

api_mode = False
if ('PANGOCFFI_API_MODE' in os.environ and
        int(os.environ['PANGOCFFI_API_MODE']) == 1):
    # Allow explicit disable of api_mode
    api_mode = True

# Create an empty _generated folder if needed
if not api_mode:
    (Path(__file__).parent / '_generated').mkdir(exist_ok=True)

# Because we can't directly load the instance builder (it would run
# ``__init__.py`` for any module import) we have to do this dubious import.
spec = importlib.util.spec_from_file_location(
    'ffi_instance_builder',
    str(Path(__file__).parent / 'ffi_instance_builder.py')
)
ffi_instance_builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ffi_instance_builder)

# Generate the bindings
ffiBuilder = ffi_instance_builder.FFIInstanceBuilder(
    source='pangocffi._generated.ffi' if not api_mode else None
)
ffi = ffiBuilder.generate()

if __name__ == '__main__':
    ffi.compile()
