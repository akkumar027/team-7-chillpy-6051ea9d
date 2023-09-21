from unittest import TestCase
from levelup.position import Position
from levelup.controller import GameController
from levelup.character import Character
from levelup.controller import Direction

class TestGameMap(TestCase):
    def test_get_position(self):
       pass 
    def test_init(self):
        testDirection = Direction()
        assert testDirection.direction != None
