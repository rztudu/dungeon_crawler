import pygame


RARITY_COLORS = {
    "Common": (220, 220, 220),
    "Rare": (50, 120, 255),
    "Epic": (180, 50, 255),
    "Legendary": (255, 170, 0),
}


class UI:

    def __init__(self):
        self.font = pygame.font.Font(None, 36)

        self.loot_item = None
        self.loot_timer = 0

        self.show_stats = False


    def update(self, dt):

        if self.loot_timer > 0:
            self.loot_timer -= dt

            if self.loot_timer <= 0:
                self.loot_item = None


    def draw(self, screen, player):

        self.draw_health_bar(
            screen,
            player
        )

        self.draw_loot_popup(
            screen
        )

        if self.show_stats:
            self.draw_stats_menu(
                screen,
                player
            )

    def draw_health_bar(self, screen, player):




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




    def draw_loot_popup(self, screen):

        if self.loot_item is None:
            return


        color = RARITY_COLORS.get(
            self.loot_item.rarity,
            "white"
        )


        # Position geändert:
        box = pygame.Rect(
            450,
            30,
            300,
            100
        )


        pygame.draw.rect(
            screen,
            (25,25,25),
            box
        )

        pygame.draw.rect(
            screen,
            color,
            box,
            3
        )


        title = self.font.render(
            "Chest opened!",
            True,
            "white"
        )

        name = self.font.render(
            self.loot_item.name,
            True,
            color
        )

        description = self.font.render(
            self.loot_item.description,
            True,
            "white"
        )


        screen.blit(
            title,
            (470,45)
        )

        screen.blit(
            name,
            (470,70)
        )

        screen.blit(
            description,
            (470,95)
        )

    def draw_stats_menu(self, screen, player):

        box = pygame.Rect(
            150,
            80,
            400,
            400
        )

        pygame.draw.rect(
            screen,
            "black",
            box
        )

        pygame.draw.rect(
            screen,
            "white",
            box,
            3
        )


        title = self.font.render(
            "Player Stats",
            True,
            "white"
        )

        screen.blit(
            title,
            (180,110)
        )


        stats = [
            f"Damage: {player.damage}",
            f"Max HP: {player.max_health}",
            "",
            "Inventory:"
        ]


        y = 160

        for text in stats:

            rendered = self.font.render(
                text,
                True,
                "white"
            )

            screen.blit(
                rendered,
                (180,y)
            )

            y += 35


        for item in player.inventory:

            text = self.font.render(
                f"{item.name} x{item.amount}",
                True,
                "white"
            )

            screen.blit(
                text,
                (200,y)
            )

            y += 30

    def show_loot(self, item):

        self.loot_item = item
        self.loot_timer = 2.5
