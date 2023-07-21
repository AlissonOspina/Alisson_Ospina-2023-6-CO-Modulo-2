import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    def __init__(self, name, scroll):
        super().__init__()
        #Imagen
        self.image = ENEMY_1
        self.name = name
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        #Posición
        self.x_pos = random.randint(0, 550)
        self.y_pos = random.randint(20, 200)
        self.scroll = scroll
        self.initial = 0

    def update(self):
        self.y_pos += self.scroll
        if self.y_pos > SCREEN_WIDTH:
            self.y_pos = self.initial
            self.x_pos = random.randint(0, 1060)
        if self.y_pos < -5:
            self.y_pos = SCREEN_WIDTH
            self.x_pos = random.randint(0, 1060)

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))
        font = pygame.font.Font(None, 20)
        label = font.render(self.name, True, (255, 0, 0))
        screen.blit(label, (self.x_pos + 10, self.y_pos - 20))
