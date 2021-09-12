import unittest
from src.karaoke_venue import Karaoke_venue
from src.room import Room
from src.song import Song
from src.guest import Guest
from src.room import Room


class TestKaraoke_venue(unittest.TestCase):
    def setUp(self):
        self.venue = Karaoke_venue("Codeclan Karaoke" , 100)
        self.room = Room(1, 4)
        self.song = Song("Imagine", "John Lennon")
        self.guest = Guest("James", 50, self.song)
        

    def test_venue_has_name(self):
        self.assertEqual("Codeclan Karaoke", self.venue.venue_name)

    def test_venue_till_amount(self):
        self.assertEqual(100, self.venue.till)

     

       

    
    


       