import pygame
from api.EnemyManager import EnemyManager
from api.AnimatedSprite import AnimatedSprite
from api.GameObject import GameObject
from api.GameConstants import GameConstants
from api.Math import Math
from api.Circle import Circle

from game.GameData import GameData


class Star(AnimatedSprite):

	TYPE_SMALL = 1
	TYPE_MEDIUM = 2
	TYPE_BIG = 3

	TYPE_ORANGE = 4
	TYPE_BLUE = 5

	def __init__(self):
		AnimatedSprite.__init__(self)

		self.mType = Math.randomIntBetween(Star.TYPE_SMALL, Star.TYPE_BIG)
		self.mColor = Math.randomIntBetween(Star.TYPE_ORANGE, Star.TYPE_BLUE)
		scale = 1
		if self.mType == Star.TYPE_SMALL:
			scale = 0.25
		elif self.mType == Star.TYPE_MEDIUM:
			scale = 0.5
		elif self.mType == Star.TYPE_BIG:
			scale = 1

		self.mFrames = []
		i = 0

		name = ''
		if self.mColor == Star.TYPE_ORANGE:
			name = "assets\\images\\stars\\orange-star"
		elif self.mColor == Star.TYPE_BLUE:
			name = "assets\\images\\stars\\blue-star"

		while i < 4:
			tmpImg = pygame.image.load(name + str(i) + ".png").convert_alpha()
			tmpImg = pygame.transform.scale(
				tmpImg, (int(tmpImg.get_width() * scale), int(tmpImg.get_height() * scale)))
			self.mFrames.append(tmpImg)
			i += 1
		
		self.setBoundAction(GameObject.NONE)
		self.setVelX(-GameConstants.ASTRAL_SPEED)
		self.setBounds(0, 0, GameConstants.inst().SCREEN_WIDTH,
						GameConstants.inst().SCREEN_HEIGHT)

		self.initAnimation(self.mFrames, 0, 8, True)

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
