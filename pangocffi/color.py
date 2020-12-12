from . import ffi, glib, pango


class Color:
    def __init__(self, red: int, green: int, blue: int):
        self._init_pointer()
        self.red = red
        self.green = green
        self.blue = blue

    def _init_pointer(self, pointer: ffi.CData = None):
        if pointer is None:
            self._pointer = ffi.new("PangoColor *")
        else:
            self._pointer = pointer

    @classmethod
    def from_pointer(cls, pointer: ffi.CData) -> "Color":
        """
        Instantiates a :class:`Attribute` from a pointer.

        :return:
            the Attribute.
        """
        if pointer == ffi.NULL:
            raise ValueError("Null pointer")
        self = object.__new__(cls)
        cls._init_pointer(self, pointer)
        self.red = pointer.red
        self.green = pointer.green
        self.blue = pointer.blue
        return self

    def copy(self):
        """
        Make a deep copy of the ``Color`` structure.

        :return:
            a copy of :class:`Color`
        """
        new_one = pango.pango_color_copy(self._pointer)
        pointer = ffi.gc(new_one, pango.pango_color_free)
        return Color.from_pointer(pointer)

    def __copy__(self) -> "Color":
        return self.copy()

    def __deepcopy__(self, memo) -> "Color":
        return self.copy()

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, red: int):
        self._red = int(red)
        red = ffi.cast("guint16", red)
        self._pointer.red = red

    @property
    def green(self):
        return int(self._green)

    @green.setter
    def green(self, green: int):
        self._green = int(green)
        green = ffi.cast("guint16", green)
        self._pointer.green = green

    @property
    def blue(self):
        return int(self._blue)

    @blue.setter
    def blue(self, blue: int):
        self._blue = int(blue)
        blue = ffi.cast("guint16", blue)
        self._pointer.blue = blue

    def parse_color(self, spec: str) -> bool:
        """
        Fill in the fields of a color from a string
        specification. The string can either one of
        a large set of standard names. (Taken from
        the CSS specification), or it can be a
        hexadecimal value in the form '#rgb'
        '#rrggbb' '#rrrgggbbb' or '#rrrrggggbbbb'
        where 'r', 'g' and 'b' are hex digits of
        the red, green, and blue components of the
        color, respectively. (White in the four forms
        is '#fff' '#ffffff' '#fffffffff' and
        '#ffffffffffff')

        :param spec:
            a string specifying the new color
        :return:
            ``TRUE`` if parsing of the specifier succeeded,
            otherwise false.
        """
        spec = ffi.new("char[]", spec.encode("utf8"))
        ret = bool(pango.pango_color_parse(self._pointer, spec))
        if ret is True:
            self._red = int(self._pointer.red)
            self._green = int(self._pointer.green)
            self._blue = int(self._pointer.blue)

    def to_string(self):
        """
        Returns a textual specification of color in the
        hexadecimal form #rrrrggggbbbb, where r, g and b
        are hex digits representing the red, green, and
        blue components respectively.

        :return:
            string hexadecimal
        """
        string = ffi.gc(
            pango.pango_color_to_string(self._pointer),
            glib.g_free,
        )
        return ffi.string(string).decode("utf-8")

    def __eq__(self, col: "Color") -> bool:
        if isinstance(col, Color):
            return (
                self.red == col.red
                and self.green == col.green
                and self.red == self.red
            )
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Color(red={self.red},blue={self.blue},green={self.green})>"
