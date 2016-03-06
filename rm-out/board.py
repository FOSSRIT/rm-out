import os
from block import Block


class Board:

    def __init__(self, h, w):
        cells_x = w / Block.WIDTH
        cells_y = h / Block.HEIGHT
        self.field = [[None] * cells_x  for i in range(cells_y)]

        for f in self.get_files():
            print(f)
            self.add_block(f)

    def draw(self, window):
        for row in self.field:
            for cell in row:
                if cell is not None:
                    cell.draw(window)

    def get_directories(self):
        return [f for f in os.listdir('.') if not os.path.isfile(f)]

    def get_files(self):
        return [f for f in os.listdir('.') if os.path.isfile(f)]

    def add_block(self, f):
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell is None:
                    b = Block(f, y, x)
                    self.field[y][x] = b
                    return

