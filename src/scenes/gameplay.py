import pygame
import random
from src.player import Player
from src.enemy import Enemy
from src.bullet import Bullet

WIDTH = 960
HEIGHT = 540


class GameplayScene:
    def __init__(self, game):
        self.game = game
        self.player = Player((WIDTH / 2, HEIGHT / 2))
        self.enemies = []
        self.bullets = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            direction = pygame.Vector2(mx, my) - self.player.position
            self.bullets.append(Bullet(self.player.position, direction))

    def update(self, dt):
        self.player.update(dt)

        for b in self.bullets:
            b.update(dt)

        for e in self.enemies:
            e.update(dt, self.player.position)

        if random.random() < 0.02:
            self.enemies.append(Enemy((random.randint(0, WIDTH), 0)))

    def draw(self, screen):
        self.player.draw(screen)

        for b in self.bullets:
            b.draw(screen)

        for e in self.enemies:
            e.draw(screen)