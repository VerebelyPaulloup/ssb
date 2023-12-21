import sys
from typing import Any

import pygame

from player import *
from enemy import *
from block import *
from room import Room
from spriteSheet import *
from ground import *
from button import *
from attack import *
from door import *
from screwdriver import Screwdriver
from hacksaw import Hacksaw
from hammer import Hammer
import time
from laurence import Laurence


class Game:  # main game class
    screen: pygame
    clock: pygame
    font: pygame
    running: bool
    win: bool
    front: pygame
    character_spritesheet: SpriteSheet
    terrain_spritesheet: SpriteSheet
    enemy_spritesheet: SpriteSheet
    attack_spritesheet: SpriteSheet
    intro_background: pygame
    win_background: pygame
    go_background: pygame
    hacksaw_spritesheet: SpriteSheet
    hammer_spritesheet: SpriteSheet
    screwdriver_spritesheet: SpriteSheet
    door_spritesheet: SpriteSheet
    laurence_spritesheet: SpriteSheet
    player: Player

    def __init__(self):  # init the game
        pygame.init()  # init pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # set the screen
        self.clock = pygame.time.Clock()  # set the clock
        self.font = pygame.font.SysFont('Arial', 32)  # set the font
        self.running = True  # set the running variable
        self.win = False
        self.front = pygame.font.Font('freesansbold.ttf', 32)  # set the font

        self.character_spritesheet = SpriteSheet("image/s2.png")  # set the spritesheet for the character
        self.terrain_spritesheet = SpriteSheet("image/terrain.png")  # set the spritesheet for the terrain
        self.enemy_spritesheet = SpriteSheet("image/tena.sprite.png")  # set the spritesheet for the enemy
        self.attack_spritesheet = SpriteSheet("image/attack.png")  # set the spritesheet for the attack
        self.intro_background = pygame.image.load("image/SuperSamiBosse.png")  # set the intro background
        self.win_background = pygame.image.load("image/win.png")  # set the win background
        self.go_background = pygame.image.load("image/SuperSamiBossGO.png")  # set the game over background
        self.hacksaw_spritesheet = SpriteSheet("image/Scie.png")  # set the spritesheet for the hacksaw
        self.hammer_spritesheet = SpriteSheet("image/Marteau.png")  # set the spritesheet for the hammer
        self.screwdriver_spritesheet = SpriteSheet("image/Tournevis.png")  # set the spritesheet for the screwdriver
        self.door_spritesheet = SpriteSheet("image/terrain.png")  # set the spritesheet for the door
        self.laurence_spritesheet = SpriteSheet("image/s3.png")  # set the spritesheet for laurence

    def createTilemap(self):  # create the tilemap
        indiceAleatoire = random.randint(0, len(tilemap) - 1)  # choose a random tilemap from the list
        for i, row in enumerate(tilemap[indiceAleatoire]):  # for each row in the tilemap list
            for j, collumn in enumerate(row):  # for each collumn in the row list
                Ground(self, j, i)  # create a ground sprite at the position of the collumn and row
                if collumn == 'E':  # if the collumn is E (enemy)
                    Enemy(self, j, i)  # create an enemy sprite at the position of the collumn and row (j and i)
                elif collumn == 'B':  # if the collumn is B (block)
                    Block(self, j, i)  # create a block sprite at the position of the collumn and row (j and i)
                elif collumn == '_':
                    Room(self, j, i)
                elif collumn == 'T':
                    Screwdriver(self, j, i)
                elif collumn == 'S':
                    Hacksaw(self, j, i)
                elif collumn == 'M':
                    Hammer(self, j, i)
                elif collumn == 'D':
                    Door(self, j, i)
                elif collumn == 'L':
                    Laurence(self, j, i)
        self.player = Player(self, 16, 5)  # create the player sprite at the position 16, 5
        # cam dans player(mouvement) ligne de for a modifier on sait jamais

    def new(self):
        # a new game starts
        self.playing = True  # set the playing variable
        self.all_sprites = pygame.sprite.LayeredUpdates()  # set the all_sprites variable to a sprite group
        self.ennemies = pygame.sprite.LayeredUpdates()  # set the ennemies variable to a sprite group
        self.blocks = pygame.sprite.LayeredUpdates()  # set the blocks variable to a sprite group         self.ennemies = pygame.sprite.LayeredUpdates()  # set the ennemies variable to a sprite group
        self.attacks = pygame.sprite.LayeredUpdates()  # set the attacks variable to a sprite group
        self.screwdriver_group = pygame.sprite.LayeredUpdates()
        self.hacksaw_group = pygame.sprite.LayeredUpdates()
        self.hammer_group = pygame.sprite.LayeredUpdates()
        self.door = pygame.sprite.LayeredUpdates()
        self.laurence = pygame.sprite.LayeredUpdates()

        self.createTilemap()  # create the tilemap

    def events(self):  # events
        for event in pygame.event.get():  # for each event in the event list (pygame.event.get())
            if event.type == pygame.QUIT:  # if the event is QUIT
                self.running = False  # set the running variable to False (stop the game)
                self.playing = False  # set the playing variable to False (stop the game)

            if event.type == pygame.KEYDOWN:  # if the event is KEYDOWN (a key is pressed)
                if event.key == pygame.K_SPACE:  # if the key is SPACE (space bar)
                    if self.player.facing == 'up':  # if the player is facing up
                        Attack(self, self.player.rect.x,
                               self.player.rect.y - TILESIZE)  # create an attack sprite at the position of the player

                    if self.player.facing == 'down':  # if the player is facing down
                        Attack(self, self.player.rect.x,
                               self.player.rect.y + TILESIZE)  # create an attack sprite at the position of the player

                    if self.player.facing == 'left':  # if the player is facing left
                        Attack(self, self.player.rect.x - TILESIZE,
                               self.player.rect.y)  # create an attack sprite at the position of the player

                    if self.player.facing == 'right':  # if the player is facing right
                        Attack(self, self.player.rect.x + TILESIZE,
                               self.player.rect.y)  # create an attack sprite at the position of the player

    def update(self):  # update the game
        self.all_sprites.update()  # update the all_sprites group

    def draw(self):  # draw the game
        self.screen.fill((0, 0, 0))  # fill the screen with black
        self.all_sprites.draw(self.screen)  # draw the all_sprites group on the screen
        self.clock.tick(FPS)  # set the clock to 60 fps
        pygame.display.update()  # update the display

    def main(self):
        temps = time.time()
        while self.playing:  # while the game is playing
            b = time.time() - temps
            print("{0:.0f}".format(b))
            if b >= 120:
                temps = time.time()
                self.playing = False
            if self.win == True:
                self.playing = False
                self.win = False
                self.win_screen()
            self.events()  # check for events
            self.update()  # update the game
            self.draw()  # draw the game

    def game_over(self):  # game over screen
        text = self.font.render(' ', True, WHITE)  # set the text
        text_rect = text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))  # set the text rect

        restart_button = Button(460, 250, 120, 50, FOND_COLOR, BLUE_DARK, 'Restart',
                                32)  # set the restart button

        for sprite in self.all_sprites:  # for each sprite in the all_sprites group
            sprite.kill()  # kill the sprite

        while self.running:  # while the game is running
            for event in pygame.event.get():  # for each event in the event list (pygame.event.get())
                if event.type == pygame.QUIT:  # if the event is QUIT
                    self.running = False  # set the running variable to False (stop the game)

            mouse_pos = pygame.mouse.get_pos()  # get the mouse position
            mouse_pressed = pygame.mouse.get_pressed()  # get the mouse pressed

            if restart_button.is_pressed(mouse_pos, mouse_pressed):  # if the restart button is pressed
                self.new()  # start a new game
                self.main()  # start the main game loop

            self.screen.blit(self.go_background, (0, 0))  # blit the game over background
            self.screen.blit(text, text_rect)  # blit the text
            self.screen.blit(restart_button.image, restart_button.rect)  # blit the restart button
            self.clock.tick(FPS)  # set the clock to 60 fps
            pygame.display.update()  # update the display

    def intro_screen(self):  # intro screen
        intro = True  # set the intro variable to True
        title = self.front.render('Paul-loup et Salomé', True, BLUE_DARK)  # edit the title
        title_rect = title.get_rect(x=395, y=100)  # edit x and y to move the title
        play_button = Button(350, 250, 250, 100, BLUE_DARK, FOND_COLOR, 'PLAY', 60)  # edit x and y to move the button

        while intro:  # while the intro is playing
            for event in pygame.event.get():  # for each event in the event list (pygame.event.get())
                if event.type == pygame.QUIT:  # if the event is QUIT
                    intro = False  # set the intro variable to False (stop the intro)
                    self.running = False  # set the running variable to False (stop the game)
            mouse_pos = pygame.mouse.get_pos()  # get the mouse position
            mouse_pressed = pygame.mouse.get_pressed()  # get the mouse pressed
            if play_button.is_pressed(mouse_pos, mouse_pressed):  # if the play button is pressed
                intro = False  # set the intro variable to False (stop the intro)
            self.screen.blit(self.intro_background, (0, 0))  # blit the intro background
            self.screen.blit(title, title_rect)  # blit the title
            self.screen.blit(play_button.image, play_button.rect)  # blit the play button
            self.clock.tick(FPS)  # set the clock to 60 fps
            pygame.display.update()  # update the display

    def win_screen(self):  # intro screen
        intro = True  # set the intro variable to True
        title = self.front.render('win', True, BLUE_DARK)  # edit the title
        title_rect = title.get_rect(x=395, y=100)  # edit x and y to move the title
        play_button = Button(350, 250, 250, 100, BLUE_DARK, FOND_COLOR, 'PLAY', 60)  # edit x and y to move the button

        while intro:  # while the intro is playing
            for event in pygame.event.get():  # for each event in the event list (pygame.event.get())
                if event.type == pygame.QUIT:  # if the event is QUIT
                    intro = False  # set the intro variable to False (stop the intro)
                    self.running = False  # set the running variable to False (stop the game)
            mouse_pos = pygame.mouse.get_pos()  # get the mouse position
            mouse_pressed = pygame.mouse.get_pressed()  # get the mouse pressed
            if play_button.is_pressed(mouse_pos, mouse_pressed):  # if the play button is pressed
                intro = False  # set the intro variable to False (stop the intro)
            self.screen.blit(self.win_background, (0, 0))  # blit the intro background
            self.screen.blit(title, title_rect)  # blit the title
            self.screen.blit(play_button.image, play_button.rect)  # blit the play button
            self.clock.tick(FPS)  # set the clock to 60 fps
            pygame.display.update()  # update the display
