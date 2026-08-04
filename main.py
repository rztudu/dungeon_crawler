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

        for chest in level.current_room.chests:
            if chest.visible and player.rect.colliderect(chest.rect):
                chest.open(player)

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

        if level.current_room.cleared():
            for chest in level.current_room.chests:
                chest.reveal()

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

        for chest in level.current_room.chests:
            chest.draw(screen, camera)

        player.draw(screen, camera)

        for enemy in level.current_room.enemies:
            if enemy.alive:
                enemy.draw(screen, camera)




        if player.health <= 0:
            running = False

        ui_rect = pygame.Rect(
            10,
            10,
            180,
            90
        )

        pygame.draw.rect(
            screen,
            "black",
            ui_rect
        )

        pygame.draw.rect(
            screen,
            "white",
            ui_rect,
            2
        )

        # HP bar
        bar_x = 20
        bar_y = 20
        bar_width = 160
        bar_height = 20

        # Background
        pygame.draw.rect(
            screen,
            "darkred",
            pygame.Rect(
                bar_x,
                bar_y,
                bar_width,
                bar_height
            )
        )

        # current HP
        health_ratio = player.health / player.max_health

        pygame.draw.rect(
            screen,
            "green",
            pygame.Rect(
                bar_x,
                bar_y,
                bar_width * health_ratio,
                bar_height
            )
        )

        # Außenrahmen
        pygame.draw.rect(
            screen,
            "white",
            pygame.Rect(
                bar_x,
                bar_y,
                bar_width,
                bar_height
            ),
            2
        )

        # HP Separator Lines
        health_step = 1

        for i in range(1, player.max_health, health_step):
            x = bar_x + (bar_width / player.max_health) * i

            pygame.draw.line(
                screen,
                "black",
                (x, bar_y),
                (x, bar_y + bar_height),
                1
            )


        '''
        bar_width = 160
        bar_height = 20

        health_ratio = player.health /player.max_health

        background_rect = pygame.Rect(
            20,
            20,
            bar_width,
            bar_height
        )

        health_rect = pygame.Rect(
            20,
            20,
            bar_width * health_ratio,
            bar_height
        )

        pygame.draw.rect(
            screen,
            "darkred",
            background_rect
        )

        pygame.draw.rect(
            screen,
            "green",
            health_rect
        )

        pygame.draw.rect(
            screen,
            "white",
            background_rect,
            2
        )
'''
        damage_text = font.render(
            f"Damage: {player.damage}",
            True,
            "white"
        )



        ui_surface = pygame.Surface((180,90), pygame.SRCALPHA)
        ui_surface.fill((0,0,0,150))

        screen.blit(ui_surface, (10,10))
        screen.blit(damage_text, (20,55))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
