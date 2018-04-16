import pygame
from api.Math import Math
from api.EnemyManager import EnemyManager
from api.Sprite import Sprite
from api.GameObject import GameObject
from api.GameConstants import GameConstants
from api.Circle import Circle

from game.GameData import GameData

class Planet(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        img = pygame.image.load("assets\\images\\planet.png").convert_alpha()
        self.setImage(img)
        self.setBoundAction(GameObject.NONE)
        self.setVelX(-5)
        self.setBounds(0, 0, GameConstants.inst().SCREEN_WIDTH,
                    GameConstants.inst().SCREEN_HEIGHT)
        self.setScore(50)

    def collides(self, player):
        return Math.collides(Circle(self.getX() + self.getWidth() / 2, self.getY() + self.getHeight() / 2, self.getWidth() / 2), player)

    def update(self):
        Sprite.update(self)

        if(self.right() < 0):
            self.die()

    def render(self, aScreen):
        Sprite.render(self, aScreen)

    def destroy(self):
        Sprite.destroy(self)
