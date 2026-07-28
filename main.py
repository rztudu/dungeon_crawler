import pygame
from camera import Camera
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from level import Level
from player import Player
from wall import Wall


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    clock = pygame.time.Clock()

    player = Player(250,250)
    enemy = Enemy(300, 200)
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    level = Level()

    running = True

    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt, level.walls)
        camera.update(player)
        enemy.update(player, dt)

        screen.fill("black")
        for wall in level.walls:
            wall.draw(screen, camera)
        player.draw(screen, camera)
        enemy.draw(screen, camera)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
