import pygame
from config import *
from inventory import *


class Door(pygame.sprite.Sprite):
    game: object
    _layer: int
    groups: object
    x: int
    y: int
    width: int
    height: int
    x_change: int
    y_change: int
    inventory: object
    image: object
    rect: object

    def __init__(self, game, x, y):
        self.game = game
        self._layer = DOOR_LAYER
        self.groups = self.game.all_sprites, self.game.door
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 35
        self.height = 35

        self.x_change = 0
        self.y_change = 0

        self.inventory = Inventory()

        self.image = self.game.door_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

