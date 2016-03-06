import os
from block import Block
from ball import Ball
from paddle import Paddle

class Board:

    def __init__(self, window):

        self.window = window
        self.h, self.w = window.getmaxyx()

        self.cells_x = self.w / Block.WIDTH
        self.cells_y = self.h / Block.HEIGHT
        self.field = [[None] * self.cells_x  for i in range(self.cells_y)]

        self._gen_blocks()
        self.ball = Ball(self.h-2, self.w/2)

        self.paddle = Paddle(self.h-1, self.w/2)

    def draw(self):
        for row in self.field:
            for cell in row:
                if cell is not None:
                    cell.draw(self.window)

        self.ball.draw(self.window)
        self.paddle.draw(self.window)

    def move(self, offset):
        self.paddle.move(offset, self.w)

    def animate(self):
        self.ball.animate(self.h, self.w)
        # self._collide_endzone()
        self._collide_blocks()
        self._collide_paddle()

    def _collide_blocks(self):
        cell_x = self.ball.x / Block.WIDTH
        cell_y = self.ball.y / Block.HEIGHT

        if (cell_y >= self.cells_y) or (cell_x >= self.cells_x):
            return

        block = self.field[cell_y][cell_x]
        if block is not None:
            #block.destroy()
            self.field[cell_y][cell_x] = None # destroy the block

            # deflect the ball
            if self.ball in block:
                pass

    def _collide_endzone(self):
        if self.ball.y == self.h - 1:
            exit()

    def _collide_paddle(self):
        if self.paddle.contacts(self.ball):
            self.ball.bounce_y()

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

