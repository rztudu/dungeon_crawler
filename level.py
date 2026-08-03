from room import Room


class Level:
    def __init__(self):
        self.rooms = []

        room = Room()

        if room.player_start is None:
            raise ValueError("Room has no player start")

        self.rooms.append(room)

        self.current_room = room
