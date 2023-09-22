from unittest import TestCase
from levelup.gamemap import GameMap
'''from levelup.position import Position
from levelup.controller import GameController
from levelup.character import Character
from levelup.controller import Direction'''

class TestGameMap(TestCase):
    def test_initialization(self):
        expectedPositionNums = 100
        self.testNumOfPositions = GameMap(100)
        self.assertEqual(self.testNumOfPositions.get_numPositions(), expectedPositionNums)
        

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