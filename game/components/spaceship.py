import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.rect = self.image.get_rect()
        self.x_pos_spaceship = 250
        self.y_pos_spaceship = 50
        self.speed_x = 0

    def update(self, user_input):
        if user_input[pygame.K_RIGHT]:
            self.speed_x = 5
        elif user_input[pygame.K_LEFT]:
            self.speed_x = -5
        
        self.x_pos_spaceship += self.speed_x


    def draw(self, screen): #lo recibe como un parametro a screen
        screen.blit(self.image, (self.x_pos_spaceship, self.y_pos_spaceship)) #blit dibujar en pantalla
       
