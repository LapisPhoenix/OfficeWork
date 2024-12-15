from time import sleep
from curses import window
from officework.room import Room
from officework.notebook import Notebook
from officework.hud import Hud


class OfficeWork:
    def __init__(self, screen: window) -> None:
        self.ROOM = 0
        self.ROOMS = {
             0: Room(tasks=[], notebook=Notebook([])),
             1: Room(tasks=[], notebook=Notebook([])),
             2: Room(tasks=[], notebook=Notebook([])),
             3: Room(tasks=[], notebook=Notebook([])),
             4: Room(tasks=[], notebook=Notebook([])),
             5: Room(tasks=[], notebook=Notebook([])),
             6: Room(tasks=[], notebook=Notebook([])),
             7: Room(tasks=[], notebook=Notebook([])),
             8: Room(tasks=[], notebook=Notebook([])),
             9: Room(tasks=[], notebook=Notebook([])),
            10: Room(tasks=[], notebook=Notebook([]))
        }

        self.screen = screen
        self.INTERACTION = {}  # Who the player is talking to
        self.notebook = ...
        self.hud = Hud(self, screen)

    def draw(self):
        self.hud.draw()

    def _main_game_loop(self) -> None:
        while True:
            self.draw()
            sleep(10/60)

    def run(self) -> None:
        self._main_game_loop()
