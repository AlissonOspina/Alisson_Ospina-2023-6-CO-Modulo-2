import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE, BULLET

class Spaceship(Sprite):
    
    X_POS = (SCREEN_WIDTH //2) - 20
    Y_POS = (SCREEN_HEIGHT //2) + 200
    
    def __init__(self, name):
        self.image = SPACESHIP
        self.image_b = BULLET
    #image1
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
    #image2
        self.image_b = pygame.transform.scale(self.image_b, (40, 60))
        self.rect_b = self.image_b.get_rect()
    #texto
        self.font = pygame.font.Font(FONT_STYLE, 15)
        self.text = self.font.render(name, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
    #posición
        self.x_pos_spaceship = self.X_POS
        self.y_pos_spaceship = self.Y_POS
        self.y_pos = self.Y_POS
        self.scroll = 5
        self.stop = 0


    def shoot(self):
        self.y_pos -= 25
        if self.y_pos < 0:
            self.y_pos = self.y_pos_spaceship

    def move_up(self):
        if self.y_pos_spaceship > 0:    
            self.y_pos_spaceship -= self.scroll 
            print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje Y")    
        else:
            self.y_pos_spaceship = self.stop

    def move_down(self):
        if self.y_pos_spaceship < SCREEN_HEIGHT - 70:     #SI la posición en [Y] es menor que el alto de la pantalla -70pixeles (esto para que no tenga que rebotar para regresar a la pantalla)
            self.y_pos_spaceship += self.scroll           #Aumenta en 5 pixeles
            print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje Y")#coordenadas en (x, y)
        else:                                                                           
            self.y_pos_spaceship = 530                    #LIMITE 

    def move_right(self): #derecha
        if self.x_pos_spaceship < SCREEN_WIDTH - 40:
            self.x_pos_spaceship += self.scroll
            print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje X")
        else:
            self.x_pos_spaceship = 1060

    def move_left(self):
        if self.x_pos_spaceship > 0:
            self.x_pos_spaceship -= self.scroll
            print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje X")
        else:
            self.x_pos_spaceship = self.stop

    def update(self, events):
        if events[pygame.K_UP]:
            self.move_up()
        elif events[pygame.K_DOWN]:
            self.move_down()
        elif events[pygame.K_RIGHT]:
            self.move_right()
        elif events[pygame.K_LEFT]:
            self.move_left()
        
    def update_shoot(self):
        self.shoot()

    def draw(self, screen): #lo recibe como un parametro a screen
        screen.blit(self.image_b, (self.x_pos_spaceship + 1, self.y_pos - 40))
        screen.blit(self.image, (self.x_pos_spaceship, self.y_pos_spaceship)) #blit dibujar en pantalla
        screen.blit(self.text, (self.x_pos_spaceship + 40, self.y_pos_spaceship - 10))
        #screen.blit(self.image_b, (self.x_pos_spaceship + 1, self.y_pos_spaceship - 40))
       
