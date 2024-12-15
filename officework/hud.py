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
│     ______     │  Thomas Edison     │  Notes: 2/5        │  Time: 420:69     │
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
        self.game = game
        self.root = stdscr
        self.width = width
        self.height = height
        self.hud_window = curses.newwin(self.height, self.width, 0, 0)

    def draw(self) -> None:
        self.hud_window.clear()
        lower_hud = self.hud_window.subwin(7, 80, 18, 0)
        todo = self.hud_window.subwin(19, 20, 0, 60)
        selfie = lower_hud.subwin(7, 18, 18, 0)
        status = lower_hud.subwin(3, 62, 18, 18)
        self.hud_window.box()
        lower_hud.box()
        selfie.box()
        todo.box()
        status.box()
        todo.addstr(1, 1, " Things to Find")

        room: Room = self.game.ROOMS[self.game.ROOM]

        for i, task in enumerate(room.tasks):
            todo.addstr(2+i, 1, f"{i+1}. {task}")

        todo.refresh()
        lower_hud.refresh()
        lower_hud.refresh()
        status.refresh()
        self.hud_window.refresh()
