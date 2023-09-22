from levelup.position import Position
from levelup.gamestatus import GameStatus
class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name

    def get_name(self):
        return self.name


    def get_position(self):
        current_positon = (1,4) # Add the function to actual method
        return current_positon
