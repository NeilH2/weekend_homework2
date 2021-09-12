import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.karaoke_venue import Karaoke_venue

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Imagine", "John Lennon")
        self.guest = Guest("James", 50, self.song)

    def test_guest_has_name(self):
        self.assertEqual("James", self.guest.name) 

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest.money) 

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song, self.guest.fav_song)   


         
