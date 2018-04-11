import pygame
from api.EnemyManager import EnemyManager
from api.Sprite import Sprite

from game.GameData import GameData

class Planet(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        img = pygame.image.load("assets\\images\\planet.png").convert_alpha()
        self.setImage(img)

    def update(self):
        

    def render(self, aScreen):
        Sprite.render(self, aScreen)

    def destroy(self):
        Sprite.destroy(self)