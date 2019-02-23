from pangocffi import pango
from enum import Enum


class Style(Enum):
    NORMAL = pango.PANGO_STYLE_NORMAL
    OBLIQUE = pango.PANGO_STYLE_OBLIQUE
    ITALIC = pango.PANGO_STYLE_ITALIC


class Weight(Enum):
    THIN = pango.PANGO_WEIGHT_THIN
    ULTRALIGHT = pango.PANGO_WEIGHT_ULTRALIGHT
    LIGHT = pango.PANGO_WEIGHT_LIGHT
    SEMILIGHT = pango.PANGO_WEIGHT_SEMILIGHT
    BOOK = pango.PANGO_WEIGHT_BOOK
    NORMAL = pango.PANGO_WEIGHT_NORMAL
    MEDIUM = pango.PANGO_WEIGHT_MEDIUM
    SEMIBOLD = pango.PANGO_WEIGHT_SEMIBOLD
    BOLD = pango.PANGO_WEIGHT_BOLD
    ULTRABOLD = pango.PANGO_WEIGHT_ULTRABOLD
    HEAVY = pango.PANGO_WEIGHT_HEAVY
    ULTRAHEAVY = pango.PANGO_WEIGHT_ULTRAHEAVY


class Variant(Enum):
    NORMAL = pango.PANGO_VARIANT_NORMAL
    SMALL_CAPS = pango.PANGO_VARIANT_SMALL_CAPS


class Stretch(Enum):
    ULTRA_CONDENSED = pango.PANGO_STRETCH_ULTRA_CONDENSED
    EXTRA_CONDENSED = pango.PANGO_STRETCH_EXTRA_CONDENSED
    CONDENSED = pango.PANGO_STRETCH_CONDENSED
    SEMI_CONDENSED = pango.PANGO_STRETCH_SEMI_CONDENSED
    NORMAL = pango.PANGO_STRETCH_NORMAL
    SEMI_EXPANDED = pango.PANGO_STRETCH_SEMI_EXPANDED
    EXPANDED = pango.PANGO_STRETCH_EXPANDED
    EXTRA_EXPANDED = pango.PANGO_STRETCH_EXTRA_EXPANDED
    ULTRA_EXPANDED = pango.PANGO_STRETCH_ULTRA_EXPANDED


class FontMask(Enum):
    FAMILY = pango.PANGO_FONT_MASK_FAMILY
    STYLE = pango.PANGO_FONT_MASK_STYLE
    VARIANT = pango.PANGO_FONT_MASK_VARIANT
    WEIGHT = pango.PANGO_FONT_MASK_WEIGHT
    STRETCH = pango.PANGO_FONT_MASK_STRETCH
    SIZE = pango.PANGO_FONT_MASK_SIZE
    GRAVITY = pango.PANGO_FONT_MASK_GRAVITY


class Alignment(Enum):
    LEFT = pango.PANGO_ALIGN_LEFT
    CENTER = pango.PANGO_ALIGN_CENTER
    RIGHT = pango.PANGO_ALIGN_RIGHT


class EllipsizeMode(Enum):
    NONE = pango.PANGO_ELLIPSIZE_NONE
    START = pango.PANGO_ELLIPSIZE_START
    MIDDLE = pango.PANGO_ELLIPSIZE_MIDDLE
    END = pango.PANGO_ELLIPSIZE_END


class Gravity(Enum):
    SOUTH = pango.PANGO_GRAVITY_SOUTH
    EAST = pango.PANGO_GRAVITY_EAST
    NORTH = pango.PANGO_GRAVITY_NORTH
    WEST = pango.PANGO_GRAVITY_WEST
    AUTO = pango.PANGO_GRAVITY_AUTO


class GravityHint(Enum):
    NATURAL = pango.PANGO_GRAVITY_HINT_NATURAL
    STRONG = pango.PANGO_GRAVITY_HINT_STRONG
    LINE = pango.PANGO_GRAVITY_HINT_LINE
