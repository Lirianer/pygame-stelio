import pygame
from api.GameObject import GameObject

class Sprite(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.mImg = None
        self.mWidth = 0
        self.mHeight = 0
        self.mVisible = True
        self.mCanCollide = True
        self.mScore = 0

    def render(self, aScreen):
        if(self.mImg != None):
            if self.mVisible:
                aScreen.blit(self.mImg, (self.getX(), self.getY()))

    def setImage(self, aImg):
        self.mImg = aImg
        self.mWidth = self.mImg.get_width()
        self.mHeight = self.mImg.get_height()

    def getImage(self):
        return self.mImg

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def right(self):
        return self.getX() + self.getWidth()

    def left(self):
        return self.getX()

    def top(self):
        return self.getY()

    def bottom(self):
        return self.getY() + self.getHeight()

    def collides(self, aSprite):
        if self.getCanCollide():
            if(self.right() > aSprite.left() and self.left() < aSprite.right()
            and self.bottom() > aSprite.top() and aSprite.bottom() > self.top()):
                return True
        else:
            return False

    def setVisible(self, aVisible):
        self.mVisible = aVisible

    def isVisible(self):
        return self.mVisible

    def setCanCollide(self, aCanCollide):
        self.mCanCollide = aCanCollide

    def getCanCollide(self):
        return self.mCanCollide

    def setScore(self, aScore):
        self.mScore = aScore

    def getScore(self):
        return self.mScore

    def destroy(self):
        GameObject.destroy(self)
        self.mImg = None
