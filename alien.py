import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represent single alien"""
    def __init__(self, ai_game):
        """ initialize the alien and get starting screen"""
        super().__init__()

        self.screen = ai_game.screen

        # load the alien image and set its rect
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()


        # start new alien from top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien extact horizontal position
        self.x = float(self.rect.x)


