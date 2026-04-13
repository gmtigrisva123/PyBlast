import pygame
import random


class Enemy:
    def __init__(self, pos):
        self.position = pygame.Vector2(pos)
        self.speed = random.uniform(80, 140)
        self.radius = 12
        self.alive = True

    def update(self, dt, player_pos):
        direction = player_pos - self.position
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.position += direction * self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 100, 120), self.position, self.radius)