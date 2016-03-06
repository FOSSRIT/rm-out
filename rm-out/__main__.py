from board import Board
import curses

# runtime vars
width = 0 # chars
height = 0


def resize(window):
    global width
    global height
    height, width = window.getmaxyx()


def main(stdscr):
    resize(stdscr) # initial resize/setup

    stdscr.clear()
    curses.curs_set(0) # hide the cursor

    board = Board(height, width)
    board.draw(stdscr)

    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break;
        elif c == curses.KEY_RESIZE:
            resize(stdscr)

curses.wrapper(main)

