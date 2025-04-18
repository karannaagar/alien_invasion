import pygame
# from pygame folder , we had sprite .py file , from sprite.py we imported Sprite

from pygame.sprite import Sprite   


class Bullet(Sprite):
    """ this class defines the bullet,  fired from a ship"""
    
    def __init__(self, ai_game):
        """create a bullet object at ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # create bullet rect at 0,0 and then set correct position

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop


        # store bullet value as decimal on y axis
        self.y = float(self.rect.y)


    def update(self):
        """ move the bullet up the screen"""
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
