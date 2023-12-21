import pygame
from config import *


class Ground(pygame.sprite.Sprite):
    game: object
    __layer: int
    groups: object
    x: int
    y: int
    width: int
    height: int
    image: object
    rect: object

    def __init__(self, game, x, y):
        self.game = game
        self.__layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(220, 420, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
