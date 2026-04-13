import pygame
from src.scenes.gameplay import GameplayScene


class MenuScene:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("consolas", 50)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.game.change_scene(GameplayScene(self.game))

    def update(self, dt):
        pass

    def draw(self, screen):
        text = self.font.render("Press any key to start", True, (255, 255, 255))
        screen.blit(text, (200, 200))