import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET

class Bullet(Sprite):
    def __init__(self, x_pos_spaceship, y_pos_spaceship):
        super().__init__()
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (20, 40))
        self.rect = self.image.get_rect()
        self.x_pos = x_pos_spaceship
        self.y_pos = y_pos_spaceship
        self.scroll = 25

    #def collision(self):


    def update(self):
        self.y_pos -= self.scroll
        if self.y_pos < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos + 10, self.y_pos - 5))
        