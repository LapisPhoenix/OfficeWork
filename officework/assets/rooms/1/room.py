from typing import TYPE_CHECKING
from officework.room import Room
from officework.notebook import Notebook


if TYPE_CHECKING:
    from officework.officework import OfficeWork


class GameRoom(Room):
    def __init__(self, game: "OfficeWork"):
        super().__init__()
        self.game = game
        self.tasks = [
            "Talk to Thomas Edison",
            "Talk to Andrew Carnegie",
            "Find out about Light Bulbs",
            "Find out about Steel Mills"
        ]
        self.notebook = Notebook([
            {
                "collected": False,
                "text": "Thomas Edison made the light bulb!"
            },
            {
                "collected": False,
                "text": "Thomas Edison made the light bulb!"
            },
            {
                "collected": False,
                "text": "Thomas Edison made the light bulb!"
            }
        ])
        self.images = [
            "./officework/assets/rooms/1/1.owimg",
        ]
	
	# Refactor into Person Class + Possible Dialogue Class
	self.thomas_edison = [  # Dialogue
	    {
	        "said": False,
		"text": "...",
		"responses: [
		    "...",
		    "..."
		]
	    }
	]

    def start(self):
