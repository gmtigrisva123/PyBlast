import pygame

VIRTUAL_WIDTH = 960
VIRTUAL_HEIGHT = 540


class Bullet:
    def __init__(self, pos, direction):
        self.position = pygame.Vector2(pos)
        self.velocity = direction.normalize() * 520.0
        self.radius = 4
        self.alive = True

    def update(self, dt):
        self.position += self.velocity * dt

        if (
            self.position.x < -20
            or self.position.x > VIRTUAL_WIDTH + 20
            or self.position.y < -20
            or self.position.y > VIRTUAL_HEIGHT + 20
        ):
            self.alive = False

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 240, 120), self.position, self.radius)