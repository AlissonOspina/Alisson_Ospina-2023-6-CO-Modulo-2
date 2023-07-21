import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE
from game.components.bullet import Bullet

class Spaceship(Sprite):
    
    X_POS = (SCREEN_WIDTH //2) - 20
    Y_POS = (SCREEN_HEIGHT //2) + 200
    
    def __init__(self, name):
        self.image = SPACESHIP
        self.bullets = pygame.sprite.Group()
    #image1
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
    #texto
        self.font = pygame.font.Font(FONT_STYLE, 15)
        self.text = self.font.render(name, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
    #posición
        self.x_pos_spaceship = self.X_POS
        self.y_pos_spaceship = self.Y_POS 
        self.scroll = 5
        self.stop = 0
        self.bullets = []
 

    def update(self, events):
        if events[pygame.K_UP]:
            self.move_up()
        elif events[pygame.K_DOWN]:
            self.move_down()
        elif events[pygame.K_RIGHT]:
            self.move_right()
        elif events[pygame.K_LEFT]:
            self.move_left()
        if events[pygame.K_SPACE]:
            self.shoot()
        for bullet in self.bullets:
            bullet.update()

    def shoot(self):
        bullet = Bullet(self.x_pos_spaceship, self.y_pos_spaceship)                #instancia
        self.bullets.append(bullet)

    
    def collision(self, list_enemies):
        enemies_to_remove = []
        for bullet in self.bullets:                                
            for enemy in list_enemies:
                if bullet.rect.colliderect(enemy.rect):   
                    print(f"bullet colisiono con {enemy.name}")
                    #list_enemies.remove(enemy)       
                    #enemies_to_remove.append(enemy)
        for enemy in enemies_to_remove:
            if enemy in list_enemies:
                list_enemies.remove(enemy)

    def move_up(self):
        if self.y_pos_spaceship > 0:    
            self.y_pos_spaceship -= self.scroll 
            #print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje Y")    
        else:
            self.y_pos_spaceship = self.stop

    def move_down(self):
        if self.y_pos_spaceship < SCREEN_HEIGHT - 70:     #SI la posición en [Y] es menor que el alto de la pantalla -70pixeles (esto para que no tenga que rebotar para regresar a la pantalla)
            self.y_pos_spaceship += self.scroll           #Aumenta en 5 pixeles
            #print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje Y")#coordenadas en (x, y)
        else:                                                                           
            self.y_pos_spaceship = 530                    #LIMITE 

    def move_right(self): #derecha
        if self.x_pos_spaceship < SCREEN_WIDTH - 40:
            self.x_pos_spaceship += self.scroll
            #print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje X")
        else:
            self.x_pos_spaceship = 1060

    def move_left(self):
        if self.x_pos_spaceship > 0:
            self.x_pos_spaceship -= self.scroll
            print(f"ES: {self.x_pos_spaceship, self.y_pos_spaceship} cambia eje X")
        else:
            self.x_pos_spaceship = self.stop

    def draw(self, screen): #lo recibe como un parametro a screen
        for bullet in self.bullets:
            bullet.draw(screen)        
        screen.blit(self.image, (self.x_pos_spaceship, self.y_pos_spaceship)) #blit dibujar en pantalla
        screen.blit(self.text, (self.x_pos_spaceship + 40, self.y_pos_spaceship - 10))
        

       
