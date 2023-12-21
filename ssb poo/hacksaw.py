import pygame
from config import *


class Hacksaw(pygame.sprite.Sprite):
    game: object
    _layer: int
    groups: object
    x: int
    y: int
    width: int
    height: int
    x_change: int
    y_change: int
    image: object
    rect: object
    state: int

    def __init__(self, game, x, y):
        self.game = game
        self._layer = INVENTORY_LAYER
        self.groups = self.game.all_sprites, self.game.hacksaw_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.image = self.game.hacksaw_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.state = 0

    def update(self):
        self.updatestate(self.game.player)
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def updatestate(self, player):
        if self.rect.colliderect(player.rect):
            self.state = 1
            self.kill()
            print("hacksaw collected")
            self.game.player.inventory.add(2)
            print(self.game.player.getInventory())
            return self.state
        else:
            return self.state
