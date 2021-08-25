from settings import Settings
from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    """Bullet control class"""

    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Bullet movement up"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)