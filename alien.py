import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represent single alien"""
    def __init__(self, ai_game):
        """ initialize the alien and get starting screen"""
        super().__init__()

        self.screen = ai_game.screen

        self.settings = ai_game.settings

        # load the alien image and set its rect
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()


        # start new alien from top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien extact horizontal position
        self.x = float(self.rect.x)


    def check_edges(self):
        """ return true , if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
            return True
        

    def update(self):
        """ move the alien to left or right"""
        self.x += ( self.settings.alien_speed * self.settings.fleet_direction )
        self.rect.x += self.x
