
class Paddle:

    PADDLE = "==========="

    def __init__(self, y, x):
        self.x = x
        self.y = y

    def draw(self, window):
        window.addstr(self.y, self.x, self.PADDLE)

    def move(self, offset, w):
        self.x += offset

        # clamp the paddle to the width of the screen
        if self.x < 0:
            self.x = 0
        elif self.x + len(self.PADDLE) >= w:
            self.x = w - len(self.PADDLE) - 1

