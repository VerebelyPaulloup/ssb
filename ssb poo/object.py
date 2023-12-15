import pygame
from config import *


class Object:
    __name: str

    def __init__(self, name, game, x, y):
        self.name = name
        self.game = game
        self._layer = OBJECT_LAYER
        self.groups = self.game.all_sprites, self.game.ennemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
