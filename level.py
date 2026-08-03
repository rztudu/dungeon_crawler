from level_map import ROOM_1, ROOM_2
from room import Room


class Level:
    def __init__(self):
        self.rooms = [
            Room(ROOM_1),
            Room(ROOM_2),
        ]

        self.current_room_index = 0
        self.current_room = self.rooms[0]

    def next_room(self):
        self.current_room_index += 1

        if self.current_room_index >= len(self.rooms):
            self.current_room_index = 0

        self.current_room = self.rooms[
            self.current_room_index
        ]
