from officework.notebook import Notebook
from engine.text.owimage import OWImage


class Room:
    def __init__(self):
        self.tasks = []
        self.notebook = Notebook([])
        self.view = OWImage()