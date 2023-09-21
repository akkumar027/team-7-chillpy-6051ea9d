from unittest import TestCase
from levelup.position import Position

class TestPositionInitWithCoordinates(TestCase):
    def test_init(self):
       CurrentPosition = (-1,-1)
       #testobj = Position(CurrentPosition[0],CurrentPosition[1])
       testobj = Position()
       self.assertEqual(CurrentPosition, testobj.coordinates)
       