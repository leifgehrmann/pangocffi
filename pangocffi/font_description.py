import ctypes
from . import pango, ffi
from . import Style, Variant, Weight, Stretch, Gravity


class FontDescription(object):

    def __init__(self):
        self._init_pointer(pango.pango_font_description_new())

    def _init_pointer(self, pointer: ctypes.c_void_p):
        self._pointer = pointer
        # self._pointer = ffi.gc(pointer, pango.pango_font_description_free)

    def get_pointer(self) -> ctypes.c_void_p:
        return self._pointer

    @classmethod
    def from_pointer(cls, pointer: ctypes.c_void_p) -> 'FontDescription':
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    def __eq__(self, other):
        if isinstance(other, FontDescription):
            return self.get_pointer() == other.get_pointer()
        return NotImplemented

    def set_family(self, family: str) -> None:
        family_pointer = ffi.new('char[]', family.encode('utf8'))
        pango.pango_font_description_set_family(self._pointer, family_pointer)

    def get_family(self) -> str:
        family_pointer = pango.pango_font_description_get_family(self._pointer)
        return ffi.string(family_pointer).decode()

    def set_style(self, style: Style) -> None:
        pango.pango_font_description_set_style(self._pointer, style.value)

    def get_style(self) -> Style:
        return Style(pango.pango_font_description_get_style(self._pointer))

    def set_variant(self, variant: Variant) -> None:
        pango.pango_font_description_set_variant(self._pointer, variant.value)

    def get_variant(self) -> Variant:
        return Variant(pango.pango_font_description_get_variant(self._pointer))

    def set_weight(self, weight: Weight) -> None:
        pango.pango_font_description_set_weight(self._pointer, weight.value)

    def get_weight(self) -> Weight:
        return Weight(pango.pango_font_description_get_weight(self._pointer))

    def set_stretch(self, stretch: Stretch) -> None:
        pango.pango_font_description_set_stretch(self._pointer, stretch.value)

    def get_stretch(self) -> Stretch:
        return Stretch(pango.pango_font_description_get_stretch(self._pointer))

    def set_size(self, size: int) -> None:
        pango.pango_font_description_set_size(self._pointer, size)

    def get_size(self) -> int:
        return pango.pango_font_description_get_size(self._pointer)

    def set_absolute_size(self, size: float) -> None:
        pango.pango_font_description_set_absolute_size(self._pointer, size)

    def get_size_is_absolute(self) -> bool:
        return pango.pango_font_description_get_size_is_absolute(self._pointer)

    def set_gravity(self, gravity: Gravity) -> None:
        pango.pango_font_description_set_gravity(self._pointer, gravity.value)

    def get_gravity(self) -> Gravity:
        return Gravity(pango.pango_font_description_get_gravity(self._pointer))
