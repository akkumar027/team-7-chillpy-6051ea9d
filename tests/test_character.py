from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap

class TestCharacter(TestCase):
    def setUp(self):
        ARBITRARY_NAME = "Bob"
        self.testobj = Character(ARBITRARY_NAME)
        self.map
        
    def test_character_not_empty(self):
        self.assertGreater(len(self.testobj.get_name()), 0)

    def test_character_same_name(self):
        ARBITRARY_NAME = "Bob"
        self.assertEqual(self.testobj.get_name(), ARBITRARY_NAME)

