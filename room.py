from chest import Chest
from constants import TILE_SIZE
from door import Door
from enemy import Enemy
from wall import Wall


class Room:
    def __init__(self, level_map):
        self.level_map = level_map

        self.walls = []
        self.enemies = []
        self.doors = []
        self.chests = []
        self.player_start: tuple[float, float] | None = None
        self.locked = True

        self.load_map()

    def load_map(self):
        for y, row in enumerate(self.level_map):
            for x, tile in enumerate(row):


                position_x = x * TILE_SIZE
                position_y = y * TILE_SIZE

                if tile == "#":
                    self.walls.append(
                        Wall(
                            position_x,
                            position_y,
                            TILE_SIZE,
                            TILE_SIZE
                        )
                    )

                elif tile == "E":
                    self.enemies.append(
                        Enemy(
                            position_x,
                            position_y
                        )
                    )

                elif tile == "P":
                    self.player_start = (
                        position_x + TILE_SIZE / 2,
                        position_y + TILE_SIZE / 2,
                    )

                elif tile == "D":

                    self.doors.append(
                        Door(
                        position_x,
                        position_y
                        )
                    )

                elif tile == "C":
                    self.chests.append(
                        Chest(
                            position_x,
                            position_y
                        )
                    )

        if self.player_start is None:
            raise ValueError("No player start 'P' found in Level_Map")

    def cleared(self):
        return len(self.enemies) == 0
