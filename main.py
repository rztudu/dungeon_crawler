import pygame
from camera import Camera
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from wall import Wall


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    clock = pygame.time.Clock()

    player = Player(400,300)
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    walls = [
        Wall(200, 150, 400, 32),
        Wall(200, 450, 400, 32),
        Wall(200, 150, 32, 332),
        Wall(568, 150, 32, 332)
    ]

    running = True

    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt, walls)
        camera.update(player)

        screen.fill("black")
        for wall in walls:
            wall.draw(screen, camera)
        player.draw(screen, camera)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
