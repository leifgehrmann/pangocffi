from . import ffi, gobject


class LayoutRun:
    def _init_pointer(self, pointer: ffi.CData):
        self._pointer = pointer

    @classmethod
    def from_pointer(cls, pointer: ffi.CData) -> 'LayoutRun':
        """
        Instantiates a :class:`LayoutRun` from a pointer.

        :return:
            the layout run.
        """
        if pointer == ffi.NULL:
            raise ValueError('Null pointer')
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        return self

    def get_pointer(self) -> ffi.CData:
        """
        Returns the pointer to this layout run.

        :return:
            a pointer to the layout run.
        """
        return self._pointer

    def get_num_chars(self) -> int:
        return self._pointer.item.num_chars
