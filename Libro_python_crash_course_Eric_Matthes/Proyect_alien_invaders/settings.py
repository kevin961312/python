import pygame
import pygame.display

class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        pygame.display.init()
        measure = pygame.display.set_mode((0, 0))
        self.screen_width = measure.get_width()
        self.screen_height = measure.get_height()
        # Background
        self.background = pygame.image.load('images/background_1.jpg')
        #self.background = pygame.image.load('images/background_2.png')
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed= 3
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 5

        #Alien settings 
        self.alien_speed = 2.0
        self.fleet_drop_speed = 3.0

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        