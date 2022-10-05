from . import ffi, glib, pango
from . import PangoObject


class Color(PangoObject):
    _INIT_METHOD = ffi.new
    _INIT_CLASS = "PangoColor"

    def __init__(self, red: int, green: int, blue: int):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_pointer(cls, pointer: ffi.CData) -> "Color":
        """
        Instantiates a :class:`Color` from a pointer.

        :return:
            the color.
        """

        self: Color = super().from_pointer(pointer)
        self.red = pointer.red
        self.green = pointer.green
        self.blue = pointer.blue

        return self

    def _get_red(self):
        return self._red

    def _set_red(self, red: int):
        self._red = int(red)
        red = ffi.cast("guint16", red)
        self._pointer.red = red

    red: int = property(_get_red, _set_red)
    """The `red` component for the color."""

    def _get_green(self):
        return int(self._green)

    def _set_green(self, green: int):
        self._green = int(green)
        green = ffi.cast("guint16", green)
        self._pointer.green = green

    green: int = property(_get_green, _set_green)
    """The `green` component for the color."""

    def _get_blue(self):
        return int(self._blue)

    def _set_blue(self, blue: int):
        self._blue = int(blue)
        blue = ffi.cast("guint16", blue)
        self._pointer.blue = blue

    blue: int = property(_get_blue, _set_blue)
    """The `blue` component for the color."""

    def parse_color(self, spec: str) -> bool:
        """
        Fill in the fields of the color from a string specification. The string
        can be any CSS color name, hexadecimal value in the form `#RGB`,
        `#RRGGBB` `#RRRGGGBBB` or `#RRRRGGGGBBBB`.

        :param spec:
            the string specifying the new color
        :return:
            whether parsing the specifier succeeded
        """
        spec = ffi.new("char[]", spec.encode("utf8"))
        ret = bool(pango.pango_color_parse(self._pointer, spec))
        if ret is True:
            self._red = int(self._pointer.red)
            self._green = int(self._pointer.green)
            self._blue = int(self._pointer.blue)

    def to_string(self):
        """
        Returns a string representation of the color in the hexadecimal
        format `#RRRRGGGGBBBB`.

        :return:
            the color string
        """
        string = ffi.gc(
            pango.pango_color_to_string(self._pointer),
            glib.g_free,
        )
        return ffi.string(string).decode("utf-8")

    # TODO: remove this and go back to using _COPY_METHOD
    # See https://github.com/leifgehrmann/pangocffi/issues/49
    def copy(self) -> "Color":
        return Color(self.red, self.green, self.blue)

    def __eq__(self, other: "Color") -> bool:
        if isinstance(other, Color):
            return (
                self.red == other.red
                and self.green == other.green
                and self.blue == other.blue
            )
