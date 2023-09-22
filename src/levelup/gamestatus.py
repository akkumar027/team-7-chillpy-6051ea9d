from levelup.position import Position

class GameStatus:
    character_name = ""
    current_position = (0,0)
    move_count = 0

    def __init__(self, character_name, current_position, move_count):
        self.character_name = character_name
        self.current_position = current_position
        self.move_count = move_count