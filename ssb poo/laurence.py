import pygame

from config import *


class Laurence(pygame.sprite.Sprite):
    game: object
    layer: int
    groups: tuple
    x: int
    y: int
    width: int
    height: int
    image: pygame
    rect: pygame

    def __init__(self, game, x, y):
        self.game = game
        self._layer = END_LAYER
        self.groups = self.game.all_sprites, self.game.laurence
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 35
        self.height = 35

        self.image = self.game.laurence_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
