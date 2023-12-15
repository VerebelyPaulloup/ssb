import pygame
from config import *
import math
from inventory import Inventory
class Player (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.__layer  = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = "down"

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animate = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.up_animate = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.left_animate = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animate = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        self.inventory = Inventory()

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        self.collide_door()
        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")

        self.x_change = 0
        self.y_change = 0

        self.facing = "down"
        self.animation_loop = 1


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = "right"
        if keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = "down"


    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.ennemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def collide_door(self):
        hits = pygame.sprite.spritecollide(self, self.game.door, False)
        if hits:
            self.kill()
            self.game.playing = False


    def collide_blocks(self,direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

    def animate(self):

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = self.down_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = self.up_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = self.left_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = self.right_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1