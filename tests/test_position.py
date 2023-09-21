from unittest import TestCase
from levelup.position import Position

class TestPositionInitWithCoordinates(TestCase):

    
    def test_init(self):
       CurrentPosition = (-1,-1)
       testobj = Position(CurrentPosition["0"],CurrentPosition[1])
       self.assertEqual(CurrentPosition, testobj.coordinates)
      # self.assertFalse(CurrentPosition,testobj.coordinates)
      ''''``` def test_init(self1):
       CurrentPosition = (-1,-1)
       testobj2 = Position(CurrentPosition[11],CurrentPosition[1])
       self1.assertEqual(CurrentPosition, testobj2.coordinates)   
''''