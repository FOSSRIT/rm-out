
import curses.textpad

class Block:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 16
        self.h = 3

    def draw(self, window):
        curses.textpad.rectangle(window, self.y, \
                                         self.x, \
                                         self.y + self.h - 1, \
                                         self.x + self.w - 1)

