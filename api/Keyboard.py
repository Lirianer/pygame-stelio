import pygame


class Keyboard(object):
    mInstance = None
    mInitialized = False
    mLeftPressed = False
    mRightPressed = False
    mQPressed = False
    mQPressedPreviousFrame = False
    mSpacePressed = False
    mSpacePressedPreviousFrame = False
    pressed = [False] * 1000
    pressedPreviousFrame = [False] * 1000

    def __new__(self, *args, **kwargs):
        if (Keyboard.mInstance is None):
            Keyboard.mInstance = object.__new__(self, *args, **kwargs)
            self.init(Keyboard.mInstance)
        else:
            print("Cuidado: Keyboard no se deberia instanciar mas de una vez. Usar Keyboard.inst()")
        return Keyboard.mInstance

    @classmethod
    def inst(cls):
        if not cls.mInstance:
            return cls()
        return cls.mInstance

    def init(self):
        if(Keyboard.mInstance):
            return

        Keyboard.mInitialized = True
        Keyboard.mLeftPressed = False
        Keyboard.mRightPressed = False
        Keyboard.mSpacePressed = False
        Keyboard.mSpacePressedPreviousFrame = False
        Keyboard.pressed = [False] * 300
        Keyboard.pressedPreviousFrame = [False] * 300

    def update(self):
        Keyboard.mSpacePressedPreviousFrame = Keyboard.mSpacePressed
        Keyboard.mQPressedPreviousFrame = Keyboard.mQPressed
        Keyboard.pressedPreviousFrame = Keyboard.pressed

    def fire(self):
        return Keyboard.mSpacePressed == True and Keyboard.mSpacePressedPreviousFrame == False

    def fire2(self, key):
        return Keyboard.mQPressed == True and Keyboard.mQPressedPreviousFrame == False

    def keyDown(self, key):
        Keyboard.pressed[key] = True

        if (key == pygame.K_LEFT):
            Keyboard.mLeftPressed = True

        if (key == pygame.K_RIGHT):
            Keyboard.mRightPressed = True

        if (key == pygame.K_SPACE):
            Keyboard.mSpacePressed = True

        if key == pygame.K_q:
            Keyboard.mQPressed = True

    def keyUp(self, key):
        Keyboard.pressed[key] = False

        if (key == pygame.K_LEFT):
            Keyboard.mLeftPressed = False

        if (key == pygame.K_RIGHT):
            Keyboard.mRightPressed = False

        if (key == pygame.K_SPACE):
            Keyboard.mSpacePressed = False

        if key == pygame.K_q:
            Keyboard.mQPressed = False

    def keyPressed(self, key):
        return Keyboard.pressed[key]

    def leftPressed(self):
        return Keyboard.mLeftPressed

    def rightPressed(self):
        return Keyboard.mRightPressed

    def destroy(self):
        Keyboard.mInstance = None