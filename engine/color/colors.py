import curses
from curses import wrapper


class Colors:
    """Basic Color Schemes for OWEngine"""
    def __init__(self, screen):
        if screen is None:
            raise Exception("You must pass screen into Colors.")

        curses.start_color()

        self._screen = screen

        self._pairs = {}

        colors = {
            "RED_BLACK": (curses.COLOR_RED, curses.COLOR_BLACK),
            "RED_YELLOW": (curses.COLOR_RED, curses.COLOR_YELLOW),
            "YELLOW_BLACK": (curses.COLOR_YELLOW, curses.COLOR_BLACK),
            "WHITE_BLACK": (curses.COLOR_WHITE, curses.COLOR_BLACK),
            "BLACK_WHITE": (curses.COLOR_BLACK, curses.COLOR_WHITE),
            "GREEN_RED": (curses.COLOR_GREEN, curses.COLOR_RED),
            "RED_GREEN": (curses.COLOR_RED, curses.COLOR_GREEN),
            "GREEN_BLACK": (curses.COLOR_GREEN, curses.COLOR_BLACK),
        }

        for index, (name, (fg, bg)) in enumerate(colors.items(), start=1):
            curses.init_pair(index, fg, bg)
            self._pairs[name] = curses.color_pair(index)

    def __getattr__(self, name):
        if name in self._pairs:
            return self._pairs[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    @staticmethod
    def normalize(rgb: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(int(((value / 255) * (1000 - 0)) + 0) for value in rgb)


# For the brits
Colours =  Colors
