import pygame

# from settings import Settings

class Ship:
    """ a class to manage ship"""

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # set ship position to same position to middle of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for ship position , so you can add decimal values to it
        self.x = float(self.rect.x)





        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ update ship position based on movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
            # self.rect.x +=1

        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed
            # self.rect.x -=1

        # update rect object to self.x
        self.rect.x = self.x

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

