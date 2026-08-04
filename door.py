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

    def draw(self, screen, camera, locked):
        color = "red" if locked else "green"

        pygame.draw.rect(
            screen,
            color,
            camera.apply(self.rect),
        )
