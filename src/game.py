import pygame
from src.scenes.menu import MenuScene


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 540))
        self.clock = pygame.time.Clock()
        self.scene = MenuScene(self)

    def change_scene(self, scene):
        self.scene = scene

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.scene.handle_event(event)

            self.scene.update(dt)

            self.screen.fill((20, 20, 30))
            self.scene.draw(self.screen)

            pygame.display.flip()

        pygame.quit()