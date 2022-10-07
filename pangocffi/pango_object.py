from abc import ABC
from . import ffi


class PangoObject(ABC):
    """
    An :external:class:`AbstractBaseClass <abc.ABC>` for every object used by
    Pango.
    """

    _INIT_METHOD: ffi = None
    """
    A CFFI function that initializes the object (i.e. `pango.pango_..._new()`).
    Alternatively, `ffi.new`.
    """
    _INIT_CLASS: str = None
    """
    Only if :attr:`_INIT_METHOD` is set to `ffi.new`, a string representing
    the class name to initialize (e.g. `"PangoLayout"`).
    """
    _GC_METHOD: ffi = None
    """A CFFI function that frees the object (i.e. `pango.pango_..._free()`)"""
    _COPY_METHOD: ffi = None
    """
    A CFFI function that copies the object (i.e. `pango.pango_..._copy()`)
    """
    _EQ_METHOD: ffi = None
    """
    A CFFI function that compares the object with another
    (i.e. `pango.pango_..._equals()`)
    """
    _pointer: ffi.CData

    def __init__(self, pointer: ffi.CData = None, *init_args):
        final_pointer: ffi.CData = pointer

        if pointer is None:
            if self._INIT_METHOD == ffi.new:
                final_pointer = ffi.new(self._INIT_CLASS + " *")
            elif self._INIT_METHOD is None:
                raise NotImplementedError(
                    "Initializing this class is not supported."
                )
            else:
                final_pointer = self._INIT_METHOD(*init_args)

        self._init_pointer(final_pointer, True)

    @property
    def pointer(self) -> ffi.CData:
        """The C pointer to this object."""
        return self._pointer

    def _init_pointer(self, pointer: ffi.CData, gc: bool):
        """
        Assign the given C pointer to this object, optionally
        enabling garbage collection.

        :param pointer:
            the C pointer to use.
        :param gc:
            whether to garbage collect.
        """

        if gc and self._GC_METHOD is not None:
            self._pointer = ffi.gc(pointer, self._GC_METHOD)
        else:
            self._pointer = pointer

    @classmethod
    def from_pointer(cls,
                     pointer: ffi.CData,
                     gc: bool = False) -> "PangoObject":
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
        if self._COPY_METHOD is None:
            raise NotImplementedError
        new_pointer = self._COPY_METHOD(self._pointer)
        return self.from_pointer(new_pointer)

    def __copy__(self) -> "PangoObject":
        return self.copy()

    def __deepcopy__(self, memo) -> "PangoObject":
        return self.copy()

    def __eq__(self, other) -> bool:
        if isinstance(other, PangoObject):
            if self.pointer == other.pointer:
                return True
            if self._EQ_METHOD:
                return bool(self._EQ_METHOD(self.pointer, other.pointer))
        return False

    def __repr__(self) -> str:
        properties = vars(self).items()

        formatted = []
        for k, v in properties:
            if k != "_pointer":
                f = k.lstrip("_") + "=" + str(v)
                formatted.append(f)

        entries = ",".join(formatted)
        return f"<{self.__class__.__name__}({entries})>"
