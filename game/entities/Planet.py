import pygame
from api.Math import Math
from api.EnemyManager import EnemyManager
from api.AnimatedSprite import AnimatedSprite
from api.GameObject import GameObject
from api.GameConstants import GameConstants
from api.Circle import Circle

from game.GameData import GameData

class Planet(AnimatedSprite):

    TYPE_PLANET = 0
    TYPE_GAS = 1

    def __init__(self, aType):
        AnimatedSprite.__init__(self)
        self.setBoundAction(GameObject.NONE)
        self.setVelX(-GameConstants.ASTRAL_SPEED)
        self.setBounds(0, 0, GameConstants.inst().SCREEN_WIDTH,
                    GameConstants.inst().SCREEN_HEIGHT)

        self.mType = aType

        imageName = ''
        frameQuantity = 0
        if self.mType == Planet.TYPE_PLANET:
            imageName = "assets\\images\\planets\\planet"
            self.setScore(50)
            frameQuantity = 20
        elif self.mType == Planet.TYPE_GAS:
            imageName = "assets\\images\\planets\\gas-planet"
            self.setScore(-50)
            frameQuantity = 7

            
        self.setAngle(Math.randomIntBetween(-30, 30))
        self.mFrames = []

        i = 0
        while i < frameQuantity:
            img = pygame.image.load(
                imageName + str(i) + ".png").convert_alpha()
            self.mFrames.append(img)
            i += 1

        self.initAnimation(self.mFrames, Math.randomIntBetween(0, len(self.mFrames) - 1), Math.randomIntBetween(2, 8), True)
        
    def collides(self, player):
        return Math.collides(Circle(self.getX() + self.getWidth() / 2, self.getY() + self.getHeight() / 2, self.getWidth() / 2), player)

    def update(self):
        AnimatedSprite.update(self)

        if(self.right() < 0):
            self.die()

    def render(self, aScreen):
        AnimatedSprite.render(self, aScreen)

    def destroy(self):
        AnimatedSprite.destroy(self)
