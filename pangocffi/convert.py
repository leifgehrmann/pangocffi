from . import pango


def units_to_double(i: int) -> float:
    return pango.pango_units_to_double(i)


def units_from_double(d: float) -> int:
    return pango.pango_units_from_double(d)
