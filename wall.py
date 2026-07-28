import pygame

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, "gray", camera.apply(self.rect))
