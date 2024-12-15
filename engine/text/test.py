import curses
from curses import wrapper
from time import sleep
from engine.color.colors import Colors
from curses import newwin


def animation(stdscr: curses.window) -> None:
    min_x = 0
    max_x = 30
    current_x = max_x
    back = 0
    character = "!"
    
    while True:
        back += 1 if current_x == max_x or current_x == min_x else 0
        current_x += -1 if back % 2 else 1
        stdscr.clear()
        stdscr.addch(0, current_x, character)
        stdscr.refresh()
        sleep(1/27)


def main(stdscr: curses.window) -> None:
    colors = Colors(stdscr)



if __name__ == "__main__":
    wrapper(main)
