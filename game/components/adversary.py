import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, FONT_STYLE

class Enemy(Sprite):
    def __init__(self, name, scroll):
        super().__init__()
        #Imagen
        self.image = ENEMY_1
        self.enemy_list =[]
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        #Letra
        self.font = pygame.font.Font(FONT_STYLE, 15)
        self.text_one = self.font.render(name, True, (255, 0, 0))
        self.text_two = self.font.render(name, True, (255, 0, 0))
        self.text_rect = self.text_one, self.text_two.get_rect()
        #Posición
        self.rect_x = random.randint(0, 550)
        self.rect_y = random.randint(20, 200)
        self.scroll = scroll
  
    def enemys(self):
        for i in range(2):
            self.enemy_list.add()

    def update(self):
        pass
        #self.x_pos_spaceship = self.scroll

    def draw_text(self, screen):
        screen.blit(self.text_one, (self.rect_x + 10, self.rect_y - 20))
        screen.blit(self.text_two, (self.rect_x + 20, self.rect_y - 40))

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))



    #self.dv1 = Enemy("dv1", 10)
    #self.dv2 = Enemy("dv2", 20)