import os
import sys
import curses
import table

# initialize screen
stdscr = curses.initscr()

# disable echoing of keys
curses.noecho()

# enable keypad for not havin gto fiddle around with escape sequences
stdscr.keypad(True)


def main():
    return None


if __name__ == '__main__':

    main()

    # reset all configs made and quiting curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

    curses.endwin()
