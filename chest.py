import pygame

from constants import TILE_SIZE
from loot import generate_loot


class Chest:
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x,
            y,
            TILE_SIZE,
            TILE_SIZE,
        )

        self.opened = False
        self.visible = False
        self.item = None


    def draw(self, screen, camera):
        if not self.visible or self.opened:
            return

        pygame.draw.rect(
            screen,
            "gold",
            camera.apply(self.rect)
        )


    def open(self, player):
        if self.opened:
            return
        self.item = generate_loot()

        player.add_item(self.item)

        self.opened = True

    def reveal(self):
        self.visible = True
