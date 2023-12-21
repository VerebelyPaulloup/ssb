import pygame
from hammer import Hammer
from hacksaw import Hacksaw
from screwdriver import Screwdriver

Hammer = False
Hacksaw = False
Screwdriver = False


class Inventory:
    liste: list
    image: object
    def __init__(self):
        self.liste = [False, False, False]
        self.image = pygame.image.load("image/box.png")

    # fonction qui ajoute un objet à l'inventaire
    def add(self, object):

        if object == 0:
            self.liste[0] = True

        elif object == 2:
            self.liste[1] = True

        elif object == 1:
            self.liste[2] = True
        else:
            pass