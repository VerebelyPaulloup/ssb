import pygame
from hammer import Hammer
from hacksaw import Hacksaw
from screwdriver import Screwdriver

Hammer = False
Hacksaw = False
Screwdriver = False


class Inventory:
    def __init__(self):
        self.liste = [Hammer, Hacksaw, Screwdriver]
        self.image = pygame.image.load("image/Box.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(x=0, y=0)

    # fonction qui ajoute un objet à l'inventaire
    def add(self, Hammer, Hacksaw, Screwdriver, player):

        if player.rect.colliderect(Hammer.rect):
            if Hammer.state == 1:
                self.liste[0] = True
                Hammer.state = 2
                print(self.liste)
            elif Hammer.state == 2:
                pass
            else:
                pass

        elif player.rect.colliderect(Hacksaw.rect):
            if Hacksaw.state == 1:
                Hacksaw.liste[1] = True
                Hacksaw.state = 2
                print(Hacksaw.liste)
            elif Hacksaw.state == 2:
                pass
            else:
                pass
        elif player.rect.colliderect(Screwdriver.rect):
            if Screwdriver.state == 1:
                self.liste[2] = True
                Screwdriver.state = 2
                print(self.liste)
            elif Screwdriver.state == 2:
                pass
            else:
                pass


    def affichage(self, screen):
        k = pygame.key.get_pressed()
        if k[pygame.K_i]:
            screen.blit(self.image, self.rect)
            if self.liste[0]:
                screen.blit(pygame.transform.scale(pygame.image.load("image/Marteau.png"), (50, 50)), (100, 0))
            if self.liste[1]:
                screen.blit(pygame.transform.scale(pygame.image.load("image/Scie.png"), (50, 50)), (200, 0))
            if self.liste[2]:
                screen.blit(pygame.transform.scale(pygame.image.load("image/Tournevis.png"), (50, 50)), (300, 0))
        else:
            pass
