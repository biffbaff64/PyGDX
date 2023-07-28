

class Align:
    CENTER = 1 << 0
    TOP = 1 << 1
    BOTTOM = 1 << 2
    LEFT = 1 << 3
    RIGHT = 1 << 4

    TOP_LEFT = TOP | LEFT
    TOP_RIGHT = TOP | RIGHT
    BOTTOM_LEFT = BOTTOM | LEFT
    BOTTOM_RIGHT = BOTTOM | RIGHT

    def is_left(self, align: int):
        return align & self.LEFT

    def is_right(self, align: int):
        return align & self.RIGHT

    def is_top(self, align: int):
        return align & self.TOP

    def is_bottom(self, align: int):
        return align & self.BOTTOM

