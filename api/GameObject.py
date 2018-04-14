import sys
import pygame

class GameObject(object):

    # Comportamiento del objeto al llegar a un borde
    NONE = 0 # No tiene ninguno, el objeto sigue de largo
    STOP = 1 # El objeto se detiene al alcanzar un borde
    WRAP = 2 # El objeto aparece por el lado contrario
    BOUNCE = 3 # El objeto rebota en el borde
    DIE = 4 # El objeto se marca para ser eliminado

    # Constructor
    # Parametros
    # aImgFile: Nombre de la imagen a cargar
    def __init__(self):
        #Coordenadas del cuadrado
        self.mX = 0
        self.mY = 0

        #Velocidad
        self.mVelX = 0
        self.mVelY = 0

        #Aceleracion
        self.mAccelX = 0
        self.mAccelY = 0

        #Imagen
        self.mImg = None

        #Variables para controlar bordes
        self.mMinX = -sys.maxsize
        self.mMaxX = sys.maxsize
        self.mMinY = -sys.maxsize
        self.mMaxY = sys.maxsize

        #Comportamiento de borde del objeto. Ponemos que no tenga ninguno por defecto
        self.mBoundAction = GameObject.NONE

        self.mIsDead = False

        #Estado actual
        self.mState = 0
        self.mTimeState = 0

    # Establece posicion del objeto
    # Parametros:
    # aX, aY: Coordenadas x e y del objeto
    def setXY(self, aX, aY):
        self.mX = aX
        self.mY = aY

    # Establece la posicion en el eje X del objeto
    # Parametros:
    # aX: Coordenada x del objeto
    def setX(self, aX):
        self.mX = aX

    # Establece la posicion en el eje Y del objeto
    # Parametros:
    # aY: Coordenada Y del objeto
    def setY(self, aY):
        self.mY = aY

    # Define los limites del movimiento del objeto
    # Parametros:
    # aMinX, aMinY: Coordenadas X e Y minimas del mundo
    # aMaxX, aMaxY: Coordenadas X e Y maximas del mundo
    def setBounds(self, aMinX, aMinY, aMaxX, aMaxY):
        self.mMinX = aMinX
        self.mMinY = aMinY
        self.mMaxX = aMaxX
        self.mMaxY = aMaxY

    # Define el comportamiento al alcanzar los bordes del mundo
    def setBoundAction(self, aBoundAction):
        self.mBoundAction = aBoundAction

    # Define la velocidad en el eje X del objeto
    # parametros:
    # aVelX: Velocidad en el eje X
    def setVelX(self, aVelX):
        self.mVelX = aVelX

    # Define la velocidad en el eje Y del objeto
    # parametros:
    # aVelX: Velocidad en el eje Y
    def setVelY(self, aVelY):
        self.mVelY = aVelY

    # Define la aceleracion en el eje X del objeto
    # parametros:
    # aAccelX: Aceleracion en el eje X
    def setAccelX(self, aAccelX):
        self.mAccelX = aAccelX

    # Define la aceleracion en el eje Y del objeto
    # parametros:
    # aAccelY: Aceleracion en el eje Y
    def setAccelY(self, aAccelY):
        self.mAccelY = aAccelY

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    # Mover el objeto
    # Parametros:
    # aIncX: Cantidad de pixeles que se mueve en el horizontal
    # aIncY: Cantidad de pixeles que se mueve en el vertical
    def update(self):

        self.mTimeState += 1

        #Modificar la velocidad segun la aceleracion
        self.mVelX += self.mAccelX
        self.mVelY += self.mAccelY

        #Mover el objeto
        self.mX += self.mVelX
        self.mY += self.mVelY

        self.checkBounds()

    def checkBounds(self):
        #Si el comportamiento es NONE no se hace nada
        if self.mBoundAction == GameObject.NONE:
            return

        #Saber que bordes esta tocando el objeto
        left = (self.mX < self.mMinX)
        right = (self.mX > self.mMaxX)
        up = (self.mY < self.mMinY)
        down = (self.mY > self.mMaxY)

        #Si no toca ningun borde no hacemos nada
        if not(left or right or up or down):
            return

        #Al llegar a este punto ya sabemos que esta tocando algun borde
        #Hay que corregir la posicion y alterar la velocidad
        #dependiendo del comportamiento al chocar el borde

        #Si es WRAP aparece del lado contrario
        if(self.mBoundAction == GameObject.WRAP):
            if(left):
                self.mX = self.mMaxX
            if(right):
                self.mX = self.mMinX
            if(up):
                self.mY = self.mMaxY
            if(down):
                self.mY = self.mMinY

        #Si es STOP, BOUNCE  o DIE corregimos la posicion porque sino
        # el objeto queda con parte afuera de los limites
        else:
            if(left):
                self.mX = self.mMinX
            if(right):
                self.mX = self.mMaxX
            if(up):
                self.mY = self.mMinY
            if(down):
                self.mY = self.mMaxY

        #Si el comportamiento es STOP o DIE, el objeto se detiene
        if(self.mBoundAction == GameObject.STOP or
                self.mBoundAction == GameObject.DIE):
            self.mVelX = 0
            self.mVelY = 0
        elif(self.mBoundAction == GameObject.BOUNCE):
            if(right or left):
                self.mVelX *= -1
            if(up or down):
                    self.mVelY *= -1

        #Si el comportamiento es que muera, no se hace mas nada
        #Esto se va a  implementar mas tarde
        if(self.mBoundAction == GameObject.DIE):
            self.mIsDead = True
            return


    # Dibuja el objeto en pantalla
    # Parametros:
    # aScreen: La superficie de la pantalla en donde dibujar
    def render(self, aScreen):
        pass

    def destroy(self):
        pass

    def die(self):
        self.mIsDead = True

    def isDead(self):
        return self.mIsDead

    def stopMove(self):
        self.mVelX = 0
        self.mVelY = 0
        self.mAccelY = 0
        self.mAccelX = 0

    def getState(self):
        return self.mState

    def setState(self, aState):
        self.mState = aState
        self.mTimeState = 0

    def getTimeState(self):
        return self.mTimeState