from dataclasses import dataclass
from officework.notebook import Notebook


@dataclass
class Room:
    tasks: list[str]
    notebook: Notebook