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

    level = Level()

    player_start = level.current_room.player_start

    if player_start is None:
        raise ValueError("No player start found")

    player = Player(
        player_start[0],
        player_start[1],
    )

    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    font = pygame.font.Font(None, 36)

    running = True

    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack(level.current_room.enemies)

        player.update(dt, level.current_room.walls)

        for door in level.current_room.doors:
            if player.rect.colliderect(door.rect):

                if level.current_room.cleared():
                    level.next_room()

                    player.position = pygame.Vector2(
                        level.current_room.player_start
                    )

                break
        camera.update(player)
        for enemy in level.current_room.enemies:
            if enemy.alive:
                enemy.update(player, dt)

        level.current_room.enemies = [
            enemy
            for enemy in level.current_room.enemies
            if enemy.alive
        ]

        for enemy in level.current_room.enemies:
            if enemy.alive and enemy.rect.colliderect(player.rect):
                player.take_damage(1)

        screen.fill("black")
        for wall in level.current_room.walls:
            wall.draw(screen, camera)

        for door in level.current_room.doors:
            door.draw(
                screen,
                camera,
                not level.current_room.cleared()
            )

        player.draw(screen, camera)

        for enemy in level.current_room.enemies:
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
