class Room:

    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []

    def list_of_songs(self):
        return len(self.song_list)

    def add_to_song_list(self, song_to_add):
        self.song_list.append(song_to_add)  

    def list_of_guests(self):
        return len(self.guest_list)   

    def add_guest_to_list(self, guest_to_add):
        self.guest_list.append(guest_to_add)  

    def check_in_guest(self, guest_to_check_in_from_guest_list):
        for guest in guest_to_check_in_from_guest_list.guest_list:
            self.guest_list.append(guest) 
        guest_to_check_in_from_guest_list.clear()       

    def check_out_guest(self, guest_to_check_out):
        for guest in guest_to_check_out.guest_list:
            self.guest_list.remove(guest) 

            
                  