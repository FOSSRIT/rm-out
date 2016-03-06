import os
from block import Block
from ball import Ball

class Board:

    def __init__(self, h, w):
        cells_x = w / Block.WIDTH
        cells_y = h / Block.HEIGHT
        self.field = [[None] * cells_x  for i in range(cells_y)]

        self._gen_blocks()
        self.ball = Ball(h-2, w/2)

    def draw(self, window):
        for row in self.field:
            for cell in row:
                if cell is not None:
                    cell.draw(window)

        self.ball.draw(window)

    def _get_directories(self):
        return [f for f in os.listdir('.') if not os.path.isfile(f)]

    def _get_files(self):
        return [f for f in os.listdir('.') if os.path.isfile(f)]

    def _add_block(self, f):
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell is None:
                    b = Block(f, y, x)
                    self.field[y][x] = b
                    return

    def _gen_blocks(self):
        for f in self._get_files():
            self._add_block(f)

        for f in self._get_directories():
            self._add_block(f)

