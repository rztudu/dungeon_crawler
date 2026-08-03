import pygame

from constants import TILE_SIZE

class Door:
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x,
            y,
            TILE_SIZE,
            TILE_SIZE,
        )

    def draw(self, screen, camera):
        pygame.draw.rect(
            screen,
            "brown",
            camera.apply(self.rect),
        )
