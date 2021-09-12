import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 4)
        self.song = Song("Imagine", "John Lennon")
        self.guest = Guest("James", 50, self.song)


    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

        
    def test_list_of_songs_starts_empty(self):
        self.assertEqual(0, self.room.list_of_songs())

    def test_add_song_to_list(self):
        self.room.add_to_song_list(self.song)
        self.assertEqual(1, self.room.list_of_songs())

    def test_can_add_guest_to_guest_list(self):
        self.room.add_guest_to_list(self.guest)
        self.assertEqual(1, self.room.list_of_guests())    

    def test_check_in_guest_to_room(self):
        guest = Guest("James", 50, self.song)
        self.room.add_guest_to_list(guest)
        self.assertEqual(1, self.room.list_of_guests())  

    def test_can_check_guest_out_of_room(self):
        guest = Guest("James", 50, self.song)
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.list_of_guests())  

     

        
  

   
