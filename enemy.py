import pygame
from constants import PLAYER_SPEED

class Enemy:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.size = 32
        self.speed = 100

    @property
    def rect(self):
        return pygame.Rect(
            self.position.x,
            self.position.y,
            self.size,
            self.size,
        )

    def update(self, player, dt):
        direction = player.position - self.position

        if direction.length() > 0:
            direction = direction.normalize()

        self.position += direction * self.speed * dt

    def draw(self, screen, camera):
        pygame.draw.rect(
            screen,
            "red",
            camera.apply(self.rect)
        )
