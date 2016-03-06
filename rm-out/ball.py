
import curses

class Ball:

    BALLCHAR = "*"

    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.vx = -1
        self.vy = -1

    def draw(self, window):
        window.addch(self.y, self.x, self.BALLCHAR)

    def animate(self):
        self.x += self.vx
        self.y += self.vy

    def bounce_x(self):
        self.vx *= -1

    def bounce_y(self):
        self.vy *= -1

