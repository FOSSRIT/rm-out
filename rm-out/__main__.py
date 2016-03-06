from board import Board
import time
import curses


FRAME_RATE = 30
PADDLE_SPEED = 2


def millis():
    return int(round(time.time() * 1000))


def main(stdscr):
    stdscr.timeout(FRAME_RATE)
    curses.curs_set(0) # hide the cursor

    board = Board(stdscr)
    board.draw()

    last_frame_time = millis()

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;
        elif c == curses.KEY_LEFT:
            board.move(-PADDLE_SPEED)
        elif c == curses.KEY_RIGHT:
            board.move(PADDLE_SPEED)

        current_time = millis()
        if current_time - last_frame_time >= FRAME_RATE:
            board.animate()

        stdscr.clear()
        board.draw()

curses.wrapper(main)

