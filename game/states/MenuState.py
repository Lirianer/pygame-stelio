import pygame

from api.GameState import GameState
from api.Keyboard import Keyboard
from api.Game import Game
from api.TextSprite import TextSprite

class MenuState(GameState):

    mImgSpace = None
    mTextTitle = None
    mTextPressFire = None

    def __init__(self):
        GameState.__init__(self)
        self.mImgSpace = None
        self.mTextTitle = None
        self.mTextPressFire = None

    def init(self):
        GameState.init(self)

        #Cargar la imagen de fondo de la pantalla.
        #La imagen es de 800x600 al igual que la pantalla
        self.mImgSpace = pygame.image.load("assets/images/menu_800x600.jpg")
        self.mImgSpace = self.mImgSpace.convert()

        #Dibujar la imagen cargada en la imagen de fondo del juego
        Game.inst().setBackground(self.mImgSpace)

        self.mTextTitle = TextSprite("INVASORES", 60, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
        self.mTextTitle.setXY((Game.SCREEN_WIDTH - self.mTextTitle.getWidth()) / 2, 50)

        self.mTextPressFire = TextSprite("Pulsa [Space] para jugar...", 20, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
        self.mTextPressFire.setXY((Game.SCREEN_WIDTH - self.mTextPressFire.getWidth()) / 2, 550)

    def update(self):
        GameState.update(self)
        if Keyboard.inst().fire():
            from game.states.LevelState import LevelState
            nextState = LevelState()
            Game.inst().setState(nextState)
            return
        self.mTextTitle.update()
        self.mTextPressFire.update()

    def render(self):
        GameState.render(self)
        self.mTextTitle.render(Game.inst().getScreen())
        self.mTextPressFire.render(Game.inst().getScreen())

    def destroy(self):
        GameState.destroy(self)
        self.mImgSpace = None
        self.mTextTitle.destroy()
        self.mTextTitle = None
        self.mTextPressFire.destroy()
        self.mTextPressFire = None

