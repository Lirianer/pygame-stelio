import math
import random
from api.Rectangle import Rectangle
from api.Circle import Circle

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
    def rectangleCircleCollision(cls, aRectangle, aCircle):
        nearestX = max(aRectangle.left(), min(aCircle.getX(), aRectangle.right()))
        nearestY = max(aRectangle.top(), min(aCircle.getY(), aRectangle.bottom()))

        deltaX = aCircle.getX() - nearestX
        deltaY = aCircle.getY() - nearestY
        return (deltaX * deltaX + deltaY * deltaY) < (aCircle.getRadius() * aCircle.getRadius())

    @classmethod
    def collides(cls, object1, object2):
        if type(object1) == Rectangle and type(object2) == Rectangle:
            return Math.rectangleRectangleCollision(object1, object2)
        elif type(object1) == Rectangle and type(object2) == Circle:
            return Math.rectangleCircleCollision(object1, object2)
        elif type(object1) == Circle and type(object2) == Circle:
            return Math.circleCircleCollision(object1, object2)
        elif type(object1) == Circle and type(object2) == Rectangle:
            return Math.rectangleCircleCollision(object2, object1)

        print('NO SE ENCONTRO COLISION APROPIADA')
        return False

    @classmethod
    def distance(cls, aX1, aY1, aX2, aY2):
        return math.sqrt(((aX2 - aX1) * (aX2 - aX1)) + ((aY2 - aY1) * (aY2 - aY1)))

    @classmethod
    def clamp(cls, aValue, aMax, aMin):
        return max(min(aValue, aMax), aMin)
