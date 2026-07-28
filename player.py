import pygame
from constants import PLAYER_SIZE, PLAYER_SPEED


class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x,y)
        self.size = PLAYER_SIZE

    def update(self, dt, walls):
        keys = pygame.key.get_pressed()

        direction = pygame.Vector2(0,0)

        if keys[pygame.K_w]:
            direction.y -= 1
        if keys[pygame.K_s]:
            direction.y += 1
        if keys[pygame.K_a]:
            direction.x -= 1
        if keys[pygame.K_d]:
            direction.x += 1

        if direction.length() > 0:
            direction = direction.normalize()

        movement = direction * PLAYER_SPEED * dt

        self.position.x += movement.x

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if movement.x > 0:
                    self.position.x = wall.rect.left - self.size
                elif movement.x < 0:
                    self.position.x = wall.rect.right

        self.position.y += movement.y

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if movement.y > 0:
                    self.position.y = wall.rect.top - self.size
                elif movement.y < 0:
                    self.position.y = wall.rect.bottom

    def draw(self, screen, camera):
        pygame.draw.rect(
            screen,
            "white",
            camera.apply(self.rect)
        )

    @property
    def rect(self):
        return pygame.Rect(
            self.position.x,
            self.position.y,
            self.size,
            self.size,
        )
