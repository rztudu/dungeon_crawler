from constants import TILE_SIZE
from enemy import Enemy
from level_map import LEVEL_MAP
from wall import Wall

print(LEVEL_MAP)

class Room:
    def __init__(self):
        self.walls = []
        self.enemies = []
        self.player_start: tuple[float, float] | None = None

        self.load_map()

    def load_map(self):
        for y, row in enumerate(LEVEL_MAP):
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

        if self.player_start is None:
            raise ValueError("No player start 'P' found in Level_Map")
