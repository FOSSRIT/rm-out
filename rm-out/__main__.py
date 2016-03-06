from board import Board
import curses

FRAME_RATE = 30
PADDLE_SPEED = 2


def main(stdscr):
    stdscr.timeout(FRAME_RATE)
    curses.curs_set(0) # hide the cursor

    board = Board(stdscr)
    board.draw()

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;
        elif c == curses.KEY_LEFT:
            board.move(-PADDLE_SPEED)
        elif c == curses.KEY_RIGHT:
            board.move(PADDLE_SPEED)
        elif c == -1:
            pass
            #board.animate() # timeout reached

        stdscr.clear()
        board.draw()

curses.wrapper(main)

