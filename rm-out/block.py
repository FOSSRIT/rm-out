import curses.textpad

class Block:

    WIDTH = 16
    HEIGHT = 3

    def __init__(self, f, cell_y, cell_x):
        self.x = cell_x * self.WIDTH
        self.y = cell_y * self.HEIGHT
        self.f = f

    def draw(self, window):
        curses.textpad.rectangle(window, self.y, \
                                         self.x, \
                                         self.y + self.HEIGHT - 1, \
                                         self.x + self.WIDTH - 1)

        window.addnstr(self.y + 1, self.x + 1, self.f, self.WIDTH - 2)

    def destroy():
        pass #kill the file, destroy the block

