from block import Block
import curses


def main(stdscr):
    stdscr.clear()
    curses.curs_set(0) # hide the cursor


    b = Block()
    b.draw(stdscr)

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;

curses.wrapper(main)

