
import curses
from block import Block


def main(stdscr):
    stdscr.clear()

    b = Block()
    b.draw(stdscr)

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;

curses.wrapper(main)

