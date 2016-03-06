from board import Board
import curses

FRAME_RATE = 30


def main(stdscr):
    stdscr.timeout(FRAME_RATE)
    curses.curs_set(0) # hide the cursor

    board = Board(stdscr)
    board.draw()

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;
        elif c == -1:
            board.animate() # timeout reached

        stdscr.clear()
        board.draw()

curses.wrapper(main)

