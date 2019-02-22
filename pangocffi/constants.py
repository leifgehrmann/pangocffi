from pangocffi import pango
from enum import Enum


class Alignment(Enum):
    LEFT = pango.PANGO_ALIGN_LEFT
    CENTER = pango.PANGO_ALIGN_CENTER
    RIGHT = pango.PANGO_ALIGN_RIGHT


class EllipsizeMode(Enum):
    NONE = pango.PANGO_ELLIPSIZE_NONE
    START = pango.PANGO_ELLIPSIZE_START
    MIDDLE = pango.PANGO_ELLIPSIZE_MIDDLE
    END = pango.PANGO_ELLIPSIZE_END
