import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH

class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.x_pos_spaceship = (SCREEN_WIDTH //2) - 20
        self.y_pos_spaceship = 400
        self.scroll_x = 0
        self.initial_pos = 0

    def update(self, events):
        if events[pygame.K_RIGHT]:
            self.scroll_x = 5
        elif events[pygame.K_LEFT]:
            self.scroll_x = -5
        elif events[pygame.K_RETURN]:
            self.scroll_x = self.initial_pos
        self.x_pos_spaceship += self.scroll_x
        

        #LIMITE
        if self.x_pos_spaceship < 1 or self.x_pos_spaceship > 1054: 
            print(f"ES: {self.x_pos_spaceship}")
            self.scroll_x = self.initial_pos

    def draw(self, screen): #lo recibe como un parametro a screen
        screen.blit(self.image, (self.x_pos_spaceship, self.y_pos_spaceship)) #blit dibujar en pantalla
       
