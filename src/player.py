import pygame
from src.utils import clamp

VIRTUAL_WIDTH = 960
VIRTUAL_HEIGHT = 540


class Player:
    def __init__(self, pos):
        self.position = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 260.0
        self.radius = 14
        self.health = 3
        self.fire_cooldown = 0.0

    def update(self, dt):
        keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x += 1

        if move.length_squared() > 0:
            move = move.normalize()

        self.velocity = move * self.speed
        self.position += self.velocity * dt

        self.position.x = clamp(self.position.x, self.radius, VIRTUAL_WIDTH - self.radius)
        self.position.y = clamp(self.position.y, self.radius, VIRTUAL_HEIGHT - self.radius)

        self.fire_cooldown = max(0.0, self.fire_cooldown - dt)

    def can_fire(self):
        return self.fire_cooldown <= 0.0

    def fired(self):
        self.fire_cooldown = 0.15

    def hit(self):
        self.health = max(0, self.health - 1)

    def alive(self):
        return self.health > 0

    def draw(self, screen):
        pygame.draw.circle(screen, (90, 220, 255), self.position, self.radius)