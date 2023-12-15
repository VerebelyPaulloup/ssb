import pygame


class Hacksaw:

    def __init__(self, x, y):
        self.coordinates = x, y
        self.image = pygame.image.load("image/Scie.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(x=x, y=y)
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.state = 0

    def draw(self, screen):
        if self.state == 0:
            screen.blit(self.image, self.rect)
        elif self.state == 1:
            pass

    def updatestate(self, player):
        if self.rect.colliderect(player.rect):
            self.state = 1
