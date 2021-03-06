import pygame
from api.Math import Math
from api.Rectangle import Rectangle
from api.Circle import Circle
from api.GameObject import GameObject

class Sprite(GameObject):

    TOP_LEFT = 0
    CENTER = 1

    def __init__(self):
        GameObject.__init__(self)
        self.mImgMaster = None
        self.mImg = None
        self.mWidth = 0
        self.mHeight = 0
        self.mVisible = True
        self.mCanCollide = True
        self.mScore = 0
        self.mRegistration = Sprite.TOP_LEFT
        self.mRadius = 0
        self.mAngle = 0


    def render(self, aScreen):
        if(self.mImg != None):
            if self.mVisible:
                if self.mAngle != 0:
                    self.updateImage()

                if self.mRegistration == Sprite.TOP_LEFT:
                    aScreen.blit(self.mImg, (self.getX(), self.getY()))
                elif self.mRegistration == Sprite.CENTER:
                    aScreen.blit(self.mImg, 
                                  (self.getX() - self.getWidth()/2, 
                                  self.getY() - self.getHeight()/2))

    def setImage(self, aImg):
        self.mImg = aImg
        self.mImgMaster = aImg
        self.mWidth = self.mImg.get_width()
        self.mHeight = self.mImg.get_height()

    def updateImage(self):
        self.mImg = pygame.transform.rotate(self.mImgMaster, self.mAngle)
        self.mWidth = self.mImg.get_width()
        self.mHeight = self.mImg.get_height()

    def setAngle(self, aAngle):
        self.mAngle = aAngle

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
            if(self.mRegistration == Sprite.TOP_LEFT):
                return Math.rectangleRectangleCollision(Rectangle(self.getX(), self.getY(), self.getWidth(), self.getHeight()),
                                                            Rectangle(aSprite.getX(), aSprite.getY(), aSprite.getWidth(), aSprite.getHeight()))
            elif(self.mRegistration == Sprite.CENTER):
                return Math.circleCircleCollision(Circle(self.getX(), self.getY(), self.getRadius()), Circle(aSprite.getX(), aSprite.getY(), aSprite.getRadius()))
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

    def setRegistration(self, aRegistration):
        self.mRegistration = aRegistration
        

    def setRadius(self, aRadius):
        self.mRadius = aRadius

    def getRadius(self):
        return self.mRadius

    def destroy(self):
        GameObject.destroy(self)
        self.mImg = None
