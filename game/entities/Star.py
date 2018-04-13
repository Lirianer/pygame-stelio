import pygame
from api.EnemyManager import EnemyManager
from api.Sprite import Sprite
from api.GameObject import GameObject
from api.GameConstants import GameConstants

from game.GameData import GameData


class Star(Sprite):

	TYPE_SMALL = 1
	TYPE_MEDIUM = 2
	TYPE_BIG = 3

	def __init__(self):
		Sprite.__init__(self)
		img = pygame.image.load("assets\\images\\star.png").convert_alpha()
		self.setImage(img)
		self.setBoundAction(GameObject.NONE)
		self.setVelX(-5)
		self.setBounds(0, 0, GameConstants.inst().SCREEN_WIDTH,
						GameConstants.inst().SCREEN_HEIGHT)

	def update(self):
		Sprite.update(self)

		if(self.right() < 0):
			self.die()

	def render(self, aScreen):
		Sprite.render(self, aScreen)

	def destroy(self):
		Sprite.destroy(self)
