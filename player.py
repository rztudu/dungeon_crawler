from os import name

import pygame

from constants import (
    ATTACK_COOLDOWN,
    ATTACK_DURATION,
    PLAYER_SIZE,
    PLAYER_SPEED,
)


class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x,y)
        self.size = PLAYER_SIZE

        self.inventory = []

        self.attack_timer = 0
        self.cooldown_timer = 0
        self.facing = pygame.Vector2(1,0)
        self.max_health = 10
        self.health = self.max_health
        self.invincible_timer = 0
        self.damage = 1
        self.speed = PLAYER_SPEED

    def update(self, dt, walls):
        if self.attack_timer > 0:
            self.attack_timer -= dt

        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt

        if self.invincible_timer > 0:
            self.invincible_timer -= dt

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
            self.facing = direction

        movement = direction * self.speed * dt

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
        color = "red" if self.invincible_timer > 0 else "white"

        pygame.draw.rect(
            screen,
            color,
            camera.apply(self.rect)
        )

        if self.attack_timer > 0:
                pygame.draw.rect(
                    screen,
                    "yellow",
                    camera.apply(self.attack_rect)
                )

    @property
    def rect(self):
        return pygame.Rect(
            self.position.x,
            self.position.y,
            self.size,
            self.size,
        )

    def attack(self, enemies):
        if self.cooldown_timer > 0:
            return

        self.cooldown_timer = ATTACK_COOLDOWN
        self.attack_timer = ATTACK_DURATION

        for enemy in enemies:
            if enemy.alive and self.attack_rect.colliderect(enemy.rect):
                direction = enemy.position -self.position

                if direction.length() > 0:
                    direction = direction.normalize()

                enemy.take_damage(
                    self.damage,
                    direction * 200
                )

    @property
    def attack_rect(self):
        attack_size = self.size

        attack_x = (
            self.position.x
            + self.size /2
            + self.facing.x * self.size
            - attack_size /2
        )

        attack_y =(
            self.position.y
            + self.size /2
            + self.facing.y * self.size
            - attack_size / 2
        )

        return pygame.Rect(
            attack_x,
            attack_y,
            attack_size,
            attack_size
        )

    def take_damage(self, amount):
        if self.invincible_timer > 0:
            return

        self.health -= amount
        self.invincible_timer = 1.0

    def add_item(self, item):

        for existing_item in self.inventory:

            if (
                existing_item.name == item.name
                and existing_item.rarity == item.rarity
            ):
                existing_item.amount += 1

                item.apply(self)

                return

        self.inventory.append(item)
        item.apply(self)
