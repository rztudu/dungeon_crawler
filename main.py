import pygame

from camera import Camera
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from level import Level
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    clock = pygame.time.Clock()

    player = Player(250,250)
    enemies = [
        Enemy(300, 200),
        Enemy(500, 250),
        Enemy(350, 450)
    ]
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    level = Level()

    font = pygame.font.Font(None, 36)

    running = True

    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack(enemies)

        player.update(dt, level.walls)
        camera.update(player)
        for enemy in enemies:
            if enemy.alive:
                enemy.update(player, dt)

        for enemy in enemies:
            if enemy.alive and enemy.rect.colliderect(player.rect):
                player.take_damage(1)

        screen.fill("black")
        for wall in level.walls:
            wall.draw(screen, camera)
        player.draw(screen, camera)

        for enemy in enemies:
            if enemy.alive:
                enemy.draw(screen, camera)

        health_text = font.render(
            f"HP: {player.health}",
            True,
            "white"
        )

        if player.health <= 0:
            running = False

        screen.blit(health_text, (20,20))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
