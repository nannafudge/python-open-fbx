from enum import Enum;

class LoadFlags(Enum):
    TRIANGULATE = 1 << 0,
    IGNORE_GEOMETRY = 1 << 1,
    IGNORE_BLEND_SHAPES = 1 << 2