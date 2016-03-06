import os
import curses
from block import Block
from ball import Ball
from paddle import Paddle

class Board:

    def __init__(self, window, path="."):

        self.window = window
        self.h, self.w = window.getmaxyx()

        self.cells_x = self.w // Block.WIDTH
        self.cells_y = self.h // Block.HEIGHT
        self.field = [[None] * self.cells_x  for i in range(self.cells_y)]

        self._gen_blocks(path)
        self.ball = Ball(self.h-2, self.w//2)

        self.paddle = Paddle(self.h-1, self.w//2)

    def draw(self):
        for row in self.field:
            for cell in row:
                if cell is not None:
                    cell.draw(self.window)

        self.window.attron(curses.color_pair(1))

        self.ball.draw(self.window)
        self.paddle.draw(self.window)

    def move(self, offset):
        self.paddle.move(offset, self.w)

    def animate(self):
        self.ball.animate(self.h, self.w)
        self._collide_endzone()
        self._collide_blocks()
        self._collide_paddle()

    def _collide_blocks(self):
        cell_x = self.ball.x // Block.WIDTH
        cell_y = self.ball.y // Block.HEIGHT

        if (cell_y >= self.cells_y) or (cell_x >= self.cells_x):
            return

        block = self.field[cell_y][cell_x]
        if block is not None:

            self.field[cell_y][cell_x] = None # destroy the block

            # deflect the ball
            if (self.ball.y == block.top()) or \
               (self.ball.y == block.bottom()):
                self.ball.bounce_y()

            if (self.ball.x == block.left()) or \
               (self.ball.x == block.right()):
                self.ball.bounce_x()

            if block.isdir:
                self._gen_blocks(block.f)
            else:
                pass
                #block.destroy()

    def _collide_endzone(self):
        if self.ball.y == self.h - 1:
            exit()

    def _collide_paddle(self):
        if self.paddle.contacts(self.ball):
            self.ball.bounce_y()

    def _add_block(self, f):
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell is None:
                    b = Block(f, y, x)
                    self.field[y][x] = b
                    return

    def _gen_blocks(self, path):
        for f in os.listdir(path):
            self._add_block(os.path.join(path, f))

