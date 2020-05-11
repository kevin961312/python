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
        self.ship_limit = 3
        # Bullet settings
        self.bullet_width = 1500
        self.bullet_height = 16
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 5
        # How quickly the alien point values increase
        self.score_scale = 1.5
        # Scoring
        self.alien_points = 50
        # How quickly the game speeds up
        self.speedup_scale = 1.05
        self.initialize_dinamyc_settings()

    def initialize_dinamyc_settings(self):
        """Initialize settings that change throughout the game."""
        self.alien_speed = 0.7
        self.ship_speed = 1.1
        self.bullet_speed= 1.5
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_drop_speed = 1.3
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)                