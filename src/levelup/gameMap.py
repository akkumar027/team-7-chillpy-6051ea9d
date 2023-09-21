from controller import GameStatus, GameController
from position import Position
from controller import Direction
from character import Character

class GameMap:
    def __init__(self,numPositions):
        self.numPositions = 100

    def getPositions(self):
        coordinate = Position()
        return coordinate.coordinates
    
    def calculatePosition(self,startingPosition: Position, direction: Direction) -> None:
        current_pos = GameStatus()
        player_direction = GameController()
        if player_direction.move() == "n" or player_direction.move() == "w":
            coordinate = Position(xCoordinate, yCoordinate)

            current_pos.current_position = current_pos
        elif player_direction.move() == "e":
            coordinate = Position(xCoordinate, yCoordinate+1)
            current_pos.current_position = coordinate
        elif player_direction.move() == "s":
            coordinate = Position(xCoordinate+1, yCoordinate)
            current_pos.current_position = coordinate
        return current_pos.current_position

    def isPositionValid(coordinates: Position):
        pass
    
    totPosition = GameController()
    print(totPosition.get_total_positions())