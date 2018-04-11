import pygame

from api.Keyboard import Keyboard
from api.GameConstants import GameConstants
from api.Mouse import Mouse
from api.TextSprite import TextSprite

import gc

class Game(object):

    mInstance = None
    mInitialized = False
    mScreen = None
    mImgBackground = None
    mClock = None
    mSalir = False

    #Pantalla (estado) actual del juego
    mState = None

    SCREEN_WIDTH = 0
    SCREEN_HEIGHT = 0
    RESOLUTION = 0
    mIsFullScreen = False

    mTextPause = None
    mIsPaused = False

    def __new__(cls, *args, **kwargs):
        if (Game.mInstance is None):
            Game.mInstance = object.__new__(cls, *args, **kwargs)
            cls.init(Game.mInstance)
        else:
            print("Cuidado: Game(): No se deberia instanciar mas de una vez esta clase. Usar Game.inst()")

        return cls.mInstance

    @classmethod
    def inst(cls):
        if not cls.mInstance:
            return cls()
        return cls.mInstance

    def init(self):
        if Game.mInitialized:
            return

        Game.mInitialized = True
        Game.SCREEN_WIDTH = GameConstants.inst().SCREEN_WIDTH
        Game.SCREEN_HEIGHT = GameConstants.inst().SCREEN_HEIGHT
        Game.RESOLUTION = (Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT)

        pygame.init()
        pygame.mixer.init()
        Game.mScreen = pygame.display.set_mode(Game.RESOLUTION)
        pygame.display.set_caption("Mi Juego")
        Game.mImgBackground = pygame.Surface(self.mScreen.get_size())
        Game.mImgBackground = self.mImgBackground.convert()
        Game.mClock = pygame.time.Clock()
        Game.mSalir = False
        pygame.mouse.set_visible(False)
        Game.mState = None

        Game.mIsPaused = False
        Game.mTextPause = TextSprite("JUEGO EN PAUSA", 60, "assets/fonts/days.otf")
        Game.mTextPause.setXY((Game.SCREEN_WIDTH - Game.mTextPause.getWidth()) / 2,
                              (Game.SCREEN_HEIGHT - Game.mTextPause.getHeight()) / 2)

    def setState(self, aState):
        if Game.mState != None:
            Game.mState.destroy()
            Game.mState = None
            print(gc.collect(), "  objetos borrados")

        Game.mState = aState
        Game.mState.init()

    def gameLoop(self):
        while not self.mSalir:
            Game.mClock.tick(30)
            Keyboard.inst().update()
            Mouse.inst().update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.mSalir = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        Game.mSalir = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        Game.mIsFullScreen = not self.mIsFullScreen
                        if self.mIsFullScreen:
                            Game.mScreen = pygame.display.set_mode(Game.RESOLUTION, pygame.FULLSCREEN)
                        else:
                            Game.mScreen  = pygame.display.set_mode(Game.RESOLUTION)

                if event.type == pygame.KEYDOWN:
                    Keyboard.inst().keyDown(event.key)

                if event.type == pygame.KEYUP:
                    Keyboard.inst().keyUp(event.key)

            #Dibujar fondo
            Game.mScreen.blit(self.mImgBackground, (0,0))

            if not Game.mIsPaused:
                Game.mState.update()
            Game.mState.render()

            if Game.mIsPaused:
                Game.mTextPause.render(self.mScreen)

            pygame.display.flip()

    def setBackground(self, aBackgroundImage):
        Game.mImgBackground = None
        Game.mImgBackground = aBackgroundImage
        self.blitBackground(Game.mImgBackground)

    def blitBackground(self, aBackgroundImage):
        Game.mScreen.blit(aBackgroundImage, (0,0))

    def getScreen(self):
        return Game.mScreen

    def destroy(self):
        if Game.mState != None:
            Game.mState.destroy()
            Game.mState = None

        Game.mTextPause.destroy()
        Game.mTextPause = None

        Keyboard.inst().destroy()
        Mouse.inst().destroy()
        pygame.mouse.set_visible(True)
        Game.mInstance = None
        pygame.quit()