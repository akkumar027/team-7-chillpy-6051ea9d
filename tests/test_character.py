from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def setUp(self):
        ARBITRARY_NAME = "Bob"
        self.testobj = Character(ARBITRARY_NAME)
        
    def test_character_not_empty(self):
        self.assertGreater(len(self.testobj.get_name()), 0)

    def test_character_not_empty(self):
        ARBITRARY_NAME = "Bob"
        self.assertEqual(self.testobj.get_name(), ARBITRARY_NAME)