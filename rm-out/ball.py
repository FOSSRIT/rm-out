
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

    def animate(self, h, w):
        self.x += self.vx
        self.y += self.vy

        if (self.x <= 0) or (self.x > w - 2):
            self.bounce_x()

        if (self.y <= 0) or (self.y > h - 2):
            self.bounce_y()

    def bounce_x(self):
        self.vx *= -1

    def bounce_y(self):
        self.vy *= -1

