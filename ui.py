import pygame


class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen, player):

        ui_rect = pygame.Rect(
            10,
            10,
            250,
            130
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

        health_ratio = max(
            0,
            min(
                player.health / player.max_health,
                1
            )
        )

        pygame.draw.rect(
            screen,
            "darkred",
            (
                bar_x,
                bar_y,
                bar_width,
                bar_height
            )
        )

        pygame.draw.rect(
            screen,
            "green",
            (
                bar_x,
                bar_y,
                bar_width * health_ratio,
                bar_height
            )
        )

        pygame.draw.rect(
            screen,
            "white",
            (
                bar_x,
                bar_y,
                bar_width,
                bar_height
            ),
            2
        )

        # Damage

        damage_text = self.font.render(
            f"Damage: {player.damage}",
            True,
            "white"
        )

        screen.blit(
            damage_text,
            (20,55)
        )

        items = ", ".join(
            item.name
            for item in player.inventory
        )

        inventory_text = self.font.render(
            items,
            True,
            "White"
        )

        screen.blit(
            inventory_text,
            (20,85)
        )
