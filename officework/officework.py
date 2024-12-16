import curses
from time import sleep
from os import listdir
from curses import window, curs_set, initscr, can_change_color, use_default_colors, init_pair, color_pair, start_color
from re import search
from engine.text.owimage import OWImage
from officework.room import Room
from officework.notebook import Notebook
from officework.hud import Hud


class OfficeWork:
    def __init__(self, screen: window) -> None:
        curs_set(0)
        initscr()
        if can_change_color():
            start_color()

        use_default_colors()

        for i in range(0, curses.COLORS):
            init_pair(i + 1, i, i)

        self.ROOM = 0
        self.ROOMS = {
            #  0: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  1: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  2: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  3: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  4: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  5: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  6: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  7: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  8: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            #  9: Room(tasks=[], notebook=Notebook([]), view=OWImage()),
            # 10: Room(tasks=[], notebook=Notebook([]), view=OWImage())
        }

        self.screen = screen
        self.INTERACTION = {}  # Who the player is talking to
        self.notebook = ...
        self.hud = Hud(self, screen)
        self._start = True

    def _load_rooms(self):
        rooms = 11

        for room in range(rooms):
            room = ...

    def _start_intro(self):
        frames = listdir("officework/assets/intro/")
        frames = [f for f in frames if f.endswith(".owimg")]
        frames = sorted(frames, key=lambda x: int(search(r'\d+', x).group()))
        for file in frames:
            if file.endswith(".owimg"):
                frame = OWImage()
                frame.decode(f"officework/assets/intro/{file}", "░▒▓█▄▀▌▪□■")
                self.screen.clear()

                y = 0
                x = 0

                for pixel in frame.data:
                    red, green, blue, character, eol = pixel

                    x += 1

                    if eol:
                        y += 1
                        x = 0
                        continue

                    index = 16 + 36 * int(red / 51) + 6 * int(green / 51) + int(blue / 51)
                    self.screen.addstr(y, x, character, color_pair(index))
                self.screen.refresh()
                sleep(24/60)

    def draw(self):
        self.hud.draw()

    def _main_game_loop(self) -> None:
        while True:
            if self._start:
                # Boot!
                self._start = False
                self._start_intro()
                continue
            self.draw()
            sleep(10/60)

    def run(self) -> None:
        self._main_game_loop()
