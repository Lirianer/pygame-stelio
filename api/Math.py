import math
import random

class Math(object):

    def __new__(self, *args, **kargs):
        print("Cuidado: Math(): No se debería instanciar esta clase.")
    
    @classmethod
    def degreeToRadian(cls, aDeg):
        return aDeg * math.pi / 180
    
    @classmethod
    def radianToDegree(cls, aRad):
        return aRad * 180 / math.pi

    @classmethod
    def randomIntBetween(cls, aInt1, aInt2):
        return random.randrange(aInt1, aInt2 + 1)

    @classmethod
    def rectangleRectangleCollision(cls, aRectangle1, aRectangle2):
        return ( (aRectangle1.right() >= aRectangle2.left()) and (aRectangle1.left() <= aRectangle2.right()) and
                    aRectangle1.bottom() >= aRectangle2.top() and aRectangle1.top() <= aRectangle2.bottom())

    @classmethod
    def circleCircleCollision(cls, aCircle1, aCircle2):
        return Math.distance(aCircle1.getX(), aCircle1.getY(),
            aCircle2.getX(), aCircle2.getY()) <= aCircle1.getRadius() + aCircle2.getRadius()

    @classmethod
    def distance(cls, aX1, aY1, aX2, aY2):
        return math.sqrt( ( (aX2 - aX1) * 2) + ((aY2 - aY1) * 2))