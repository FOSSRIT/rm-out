
import curses

class Ball:

    BALLCHAR = "*"

    def __init__(self, y, x):
        self.x = x
        self.y = y

    def draw(self, window):
        window.addch(self.y, self.x, self.BALLCHAR)

