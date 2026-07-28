import pygame


class Camera:
    def __init__(self, width, height):
        self.offset = pygame.Vector2(0,0)
        self.width = width
        self.height = height

    def update(self, target):
        self.offset.x = (
            target.position.x
            - self.width / 2
        )

        self.offset.y = (
            target.position.y
            - self.height / 2
        )

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)
