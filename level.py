from wall import Wall

class Level:
    def __init__(self):
        self.walls = []

        self.create_test_room()

    def create_test_room(self):
        self.walls.append(
            Wall(100, 100, 300, 32)
        )

        self.walls.append(
            Wall(100, 100, 32, 300)
        )

        self.walls.append(
            Wall(400, 100, 32, 300)
        )

        self.walls.append(
            Wall(100, 400, 332, 32)
        )
