from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap

class TestCharacter(TestCase):

    @classmethod
    def setUpClass(cls):
        print("All my tests starts here")

    def setUp(self):
        ARBITRARY_NAME = "Bob"
        self.testobj = Character(ARBITRARY_NAME)
        
    def test_character_not_empty(self):
        self.assertGreater(len(self.testobj.get_name()), 0)

    def test_character_same_name(self):
        EXPECTED_NAME = "Bob"
        self.assertEqual(self.testobj.get_name(), EXPECTED_NAME)



