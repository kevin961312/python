import  pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_game):
        super(Alien,self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        #image = pygame.image.load('images/alien.png')
        image = pygame.image.load('Images/alien_star.png')
        self.image = pygame.transform.scale(image,(50,50))
        self.rect = self.image.get_rect()
        

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x





        