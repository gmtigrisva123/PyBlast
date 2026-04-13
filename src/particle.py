import pygame


class Particle:
    def __init__(self, pos, vel, life, color, radius):
        self.position = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(vel)
        self.life = life
        self.color = color
        self.radius = radius

    def update(self, dt):
        self.life -= dt
        self.position += self.velocity * dt
        self.velocity *= 0.98
        self.radius = max(0, self.radius - 20 * dt)

    def draw(self, screen):
        if self.life <= 0 or self.radius <= 0:
            return
        pygame.draw.circle(screen, self.color, self.position, int(self.radius))