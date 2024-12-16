"""
╭──────────────────────────────────────────────────────────────────────────────╮
│									                       │  Things to Find   │
│							                               │  1. blah	       │
│							                               │  2. Blah	       │
│							                               │				   │
│							                               │				   │
│							                               │				   │
│							                               │				   │
│							                               │				   │
│							                               │				   │
│						                                   │				   │
│						                                   │				   │
│							                               │				   │
│						                                   │				   │
│				                                           │				   │
│						                                   │				   │
│					   	                                   │				   │
⊢──────────────────────────────────────────────────────────────────────────────⊣
│     ______     │  Thomas Edison     │  Notes: 2/5        │  Time: 1:30       │
│    /      \    ⊢─────────────────────────────────────────────────────────────⊣
│    | * _ * |   │                                                             │
│     \____/     │  Yeah man I really dont know how the happened but i do kno  │
│       | |      │  w that i can hit the griddy. would you like me to sir? i   │
│     /====\     │                                                             │
│    | |==| |    │                                                             │
╰──────────────────────────────────────────────────────────────────────────────╯
"""
import curses
from typing import TYPE_CHECKING
from threading import Thread
from officework.room import Room


if TYPE_CHECKING:
    from officework.officework import OfficeWork


class Hud(Thread):
    def __init__(self, game: "OfficeWork", stdscr: curses.window, width: int = 80, height: int = 25):
        Thread.__init__(self)
        curses.initscr()
        if curses.can_change_color():
            curses.start_color()

        curses.use_default_colors()

        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, i)

        self.game = game
        self.root = stdscr
        self.width = width
        self.height = height
        self.hud_window = curses.newwin(self.height, self.width, 0, 0)

    def _refresh(self, huds):
        # Refresh windows
        for window in huds:
            window.refresh()

    def draw(self) -> None:
        self.hud_window.clear()

        lower_hud = self.hud_window.subwin(7, 80, 18, 0)
        todo = self.hud_window.subwin(19, 20, 0, 60)
        selfie = lower_hud.subwin(7, 18, 18, 0)
        status = lower_hud.subwin(3, 62, 18, 18)

        for window in [self.hud_window, lower_hud, selfie, todo, status]:
            window.box()

        todo.addstr(1, 1, " Things to Find")

        room: Room = self.game.ROOMS[self.game.ROOM]
        for i, task in enumerate(room.tasks):
            todo.addstr(2 + i, 1, f"{i + 1}. {task}")

        if room.view.data is None:
            self._refresh([todo, lower_hud, status, self.hud_window])
            return

        y = 1
        xmin = 0
        x = xmin

        # A tuple of (Red, Green, Blue, Character "Pixel", End Of Line "EoL")
        for pixel in room.view.data:
            red, green, blue, character, eol = pixel

            x += 1

            if eol:
                y += 1
                x = xmin
                continue

            try:
                index = 16 + 36 * int(red / 51) + 6 * int(green / 51) + int(blue / 51)
                self.hud_window.addstr(y, x, character, curses.color_pair(index))
            except curses.error:
                # Silently ignore drawing errors
                pass

        self._refresh([todo, lower_hud, status, self.hud_window])
