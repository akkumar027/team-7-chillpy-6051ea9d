from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.character import Character
from levelup.position import Position
from levelup.controller import Direction
'''from levelup.position import Position
from levelup.controller import GameController

from levelup.controller import Direction'''

class TestGameMap(TestCase):
    def test_initialization(self):
        expectedPositionNums = 100
        self.testNumOfPositions = GameMap(100)
        self.assertEqual(self.testNumOfPositions.get_numPositions(), expectedPositionNums)
        
    def test_position_getter(self):
        self.position_coordinate = Character("Alex")
        self.position_coordinate.get_position()

    def test_calc_position(self):
        testCurrent = (-1,-1)
        test_current_position = Position(testCurrent[0], testCurrent[1])
        self.assertEqual(testCurrent, test_current_position.coordinates)
       
        '''aPosition = (0,5)
        self.assertEqual(
            aPosition,
            testpos.numPositions'''
       
        #self.assertIsNone(testpos.)
    '''def test_get_position(self):
       testposition = Game '''
    '''def test_init(self):
        testDirection = Direction()
        assert testDirection.direction != None
'''