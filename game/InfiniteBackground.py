from pygame import *
from api.Manager import *
from api.GameConstants import GameConstants
from api.GameObject import GameObject
from api.Sprite import Sprite

class InfiniteBackground(GameObject):

    def __init__(self):
        background = pygame.image.load('assets\\images\\background.png')

        i = 0

        self.images = []

        while i < 3:
            sprite = Sprite()
            sprite.setImage(background)
            sprite.setVelX(-GameConstants.BACKGROUND_SPEED)
            sprite.setXY(i * GameConstants.SCREEN_WIDTH, 0)
            self.images.append(sprite)

            i += 1


    def update(self):
        for sprite in self.images:
            sprite.update()

            if sprite.right() < 0:
                sprite.setX((len(self.images) - 1) * GameConstants.SCREEN_WIDTH - GameConstants.BACKGROUND_SPEED)
        

    def render(self, aScreen):
        for sprite in self.images:
            sprite.render(aScreen)

    def destroy(self):
        for sprite in self.images:
            sprite.destroy()

        self.images = None
        
        
        
