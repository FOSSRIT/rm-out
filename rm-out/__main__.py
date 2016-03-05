
import curses


def main(stdscr):
    stdscr.clear()

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;

curses.wrapper(main)

