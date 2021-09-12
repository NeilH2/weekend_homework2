import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Imagine" , "John Lennon")
        

    def test_song_has_title(self):
        self.assertEqual("Imagine", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("John Lennon", self.song.artist)

        

    
