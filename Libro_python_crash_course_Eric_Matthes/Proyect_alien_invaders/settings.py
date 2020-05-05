import pygame
import pygame.locals
pygame.display.init()
measure = pygame.display.set_mode((0, 0))
class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        global measure
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 680
        # Background
        image = pygame.image.load('images/background_1.jpg')
        #image = pygame.image.load('images/background_2.png')
        self.background = image.convert_alpha()
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed= 3
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 5

        #Alien settings 
        self.alien_speed = 1
        self.fleet_drop_speed = 2

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        