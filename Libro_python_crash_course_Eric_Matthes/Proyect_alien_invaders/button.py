import pygame.font
image = pygame.image.load('images/button_play.png')
image = image.convert_alpha()
class Button:
    def __init__(self, ai_game):
        global image
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()  
        self.image = pygame.transform.scale(image, (130, 130))
        self.rect  = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
    def draw_button(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
