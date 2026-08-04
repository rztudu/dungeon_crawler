import pygame

from constants import TILE_SIZE


class Chest:
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x,
            y,
            TILE_SIZE,
            TILE_SIZE,
        )

        self.opened = False

    def draw(self, screen, camera):
        if self.opened:
            return

        pygame.draw.rect(
            screen,
            "gold",
            camera.apply(self.rect)
        )

    def open(self, player):
        if self.opened:
            return

        self.opened = True

        player.health += 1
