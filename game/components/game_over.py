import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:

    X_POS = SCREEN_WIDTH //2
    Y_POS = SCREEN_HEIGHT //2 - 80

    def __init__(self, message, screen):
        screen.fill((0, 0, 0))
        self.font = pygame.font.Font(FONT_STYLE, 80)
        self.text = self.font.render(message, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.X_POS, self.Y_POS)

    def update(self):
        pygame.display.update()

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

