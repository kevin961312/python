import pygame.font

class Button:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()  
        image = pygame.image.load('images/button_play.png')
        self.image = pygame.transform.scale(image, (150, 150))
        self.rect  = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
    def draw_button(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
