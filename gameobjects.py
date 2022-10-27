import pygame
from pygame import math

class GameObjects(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.surface = pygame.Surface((width, height))
        self.surface.fill((0, 230, 230))
        self.pos = math.Vector2(x, y - (height / 2))
        self.rect = self.surface.get_rect(center = self.pos)