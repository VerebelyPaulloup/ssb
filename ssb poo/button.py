import pygame
from config import *


class Button:
    font: pygame
    content: str
    x: int
    y: int
    width: int
    height: int
    fg: tuple
    bg: tuple
    image: pygame
    rect: pygame
    text: pygame
    text_rect: pygame

    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font("Ario.ttf", fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
