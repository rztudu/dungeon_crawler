import pygame

from camera import Camera
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from level import Level
from player import Player
from ui import UI


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        self.clock = pygame.time.Clock()

        self.level = Level()

        player_start = self.level.current_room.player_start

        self.player = Player(
            player_start[0],
            player_start[1],
        )
        print("Player HP:", self.player.health)
        print("Player max HP:", self.player.max_health)


        self.camera = Camera(
            SCREEN_WIDTH,
            SCREEN_HEIGHT
        )

        self.ui = UI()

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.attack(
                    self.level.current_room.enemies
                )


    def update(self, dt):



        self.player.update(
            dt,
            self.level.current_room.walls
        )

        room = self.level.current_room

        # Check door
        for door in room.doors:

            if self.player.rect.colliderect(door.rect) and room.cleared():

                self.level.next_room()

                self.player.position = pygame.Vector2(
                    self.level.current_room.player_start
                )

                break

        for chest in room.chests:
            if chest.visible and self.player.rect.colliderect(chest.rect):
                chest.open(self.player)

        for enemy in room.enemies:
            if enemy.alive:
                enemy.update(
                    self.player,
                    dt
                )

        room.enemies = [
            enemy
            for enemy in room.enemies
            if enemy.alive
        ]

        if room.cleared():
            for chest in room.chests:
                chest.reveal()

        for enemy in room.enemies:
            if enemy.rect.colliderect(self.player.rect):
                self.player.take_damage(1)

        self.camera.update(
            self.player
        )

        if self.player.health <= 0:
            self.running = False

    def draw(self):

        self.screen.fill("black")

        room = self.level.current_room

        # Walls
        for wall in room.walls:
            wall.draw(
                self.screen,
                self.camera
            )

        # Doors
        for door in room.doors:
            door.draw(
                self.screen,
                self.camera,
                not room.cleared()
            )

        # Chests
        for chest in room.chests:
            chest.draw(
                self.screen,
                self.camera
            )

        # Enemies
        for enemy in room.enemies:
            if enemy.alive:
                enemy.draw(
                    self.screen,
                    self.camera
                )

        self.player.draw(
            self.screen,
            self.camera
        )

        self.ui.draw(
            self.screen,
            self.player
        )

        pygame.display.flip()
