from abc import ABC
from . import ffi

class PangoObject(ABC):
    """An abstract base class for every object used by Pango."""

    _INIT_METHOD: ffi
    _INIT_CLASS: str
    _GC_METHOD: ffi
    _COPY_METHOD: ffi
    _EQ_METHOD: ffi
    _pointer: ffi.CData

    def __init__(self, pointer: ffi.CData):
        final_pointer: ffi.CData = pointer

        if pointer == None:
            if self._INIT_METHOD == ffi.new:
                final_pointer = ffi.new(self._INIT_CLASS + " *")
            elif self._INIT_METHOD == None:
                raise "Initializing this class is not supported."
            else:
                final_pointer = self._INIT_METHOD(pointer)

        self._init_pointer(final_pointer, True)

    def _get_pointer(self) -> ffi.CData:
        return self._pointer

    pointer: ffi.CData = property(_get_pointer)
    """The C pointer to this object."""

    def _init_pointer(self, pointer: ffi.CData, gc: bool):
        if gc:
            self._pointer = ffi.gc(pointer, self._GC_METHOD)
        else:
            self._pointer = pointer

    @classmethod
    def from_pointer(cls, pointer: ffi.CData, gc: bool = False) -> "PangoObject":
        """
        Instantiates an object from a C pointer.

        :param pointer:
            a C pointer to the object.
        :param gc:
            whether to garbage collect the pointer. Defaults to ``False``.
        :return:
            the object.
        """

        if pointer == ffi.NULL:
            raise ValueError("Null pointer")
        self = object.__new__(cls)
        cls._init_pointer(self, pointer, gc)

        return self

    def copy(self):
        new_pointer = self._COPY_METHOD(self._pointer)
        return self.from_pointer(new_pointer)

    def __copy__(self) -> "PangoObject":
        return self.copy()

    def __deepcopy__(self, memo) -> "PangoObject":
        return self.copy()

    def __eq__(self, other: "PangoObject") -> bool:
        if self._EQ_METHOD:
            return bool(self._EQ_METHOD(self.pointer, other.pointer))
        else:
            return self.pointer == other.pointer

    def __repr__(self) -> str:
        properties = vars(self)
        formatted = ",".join([f"{k}={self[k]}" for k in properties])
        return f"<{self.__name__}({formatted})>"
