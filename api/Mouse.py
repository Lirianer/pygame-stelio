import pygame

class Mouse(object):

    mInstance = None
    mInitialized = False
    mLeftPressed = False
    mCenterPressed = False
    mRightPressed = False
    mLeftPressedPreviousFrame = False

    def __new__(cls, *args, **kwargs):
        if Mouse.mInstance is None:
            Mouse.mInstance = object.__new__(cls, *args, **kwargs)
            cls.init(Mouse.mInstance)
        else:
            print("Cuidado: Mouse(): No se deberia instanciar mas de una vez esta clase. Usar Mouse.inst()")

        return Mouse.mInstance

    @classmethod
    def inst(cls):
        if not cls.mInstance:
            return cls()
        return cls.mInstance

    def init(self):
        if Mouse.mInitialized:
            return

        Mouse.mInitialized = True
        Mouse.mLeftPressed = False
        Mouse.mCenterPressed = False
        Mouse.mRightPressed = False
        Mouse.mLeftPressedPreviousFrame = False

    def update(self):
        Mouse.mLeftPressedPreviousFrame = Mouse.mLeftPressed
        Mouse.mLeftPressed = pygame.mouse.get_pressed()[0]
        Mouse.mCenterPressed = pygame.mouse.get_pressed()[1]
        Mouse.mRightPressed = pygame.mouse.get_pressed()[2]

    def leftPressed(self):
        return Mouse.mLeftPressed

    def rightPressed(self):
        return Mouse.mRightPressed

    def centerPressed(self):
        return Mouse.mCenterPressed

    def click(self):
        return Mouse.mLeftPressed == False and Mouse.mLeftPressedPreviousFrame == True

    def getPos(self):
        return pygame.mouse.get_pos()

    def getX(self):
        return pygame.mouse.get_pos()[0]

    def getY(self):
        return pygame.mouse.get_pos()[1]

    def destroy(self):
        Mouse.mInstance = None