import pygame
from game import Game
import sys

g = Game()  # create the game
g.intro_screen()  # start the intro screen
g.new()  # start a new game
while g.running:  # while the game is running
    g.main()  # start the main game loop
    g.game_over()  # start the game over screen

pygame.quit()  # quit pygame
sys.exit()  # quit the program
