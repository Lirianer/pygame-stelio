import pygame
from api.Math import Math
from api.EnemyManager import EnemyManager
from api.AnimatedSprite import AnimatedSprite
from api.GameObject import GameObject
from api.GameConstants import GameConstants
from api.Circle import Circle

from game.GameData import GameData

class Planet(AnimatedSprite):

    def __init__(self):
        AnimatedSprite.__init__(self)
        self.setBoundAction(GameObject.NONE)
        self.setVelX(-GameConstants.ASTRAL_SPEED)
        self.setBounds(0, 0, GameConstants.inst().SCREEN_WIDTH,
                    GameConstants.inst().SCREEN_HEIGHT)
        self.setScore(50)

        self.mFrames = []
        i = 0
        while i < 20:
            img = pygame.image.load(
                "assets\\images\\planets\\planet" + str(i) + ".png").convert_alpha()
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
