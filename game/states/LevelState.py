import pygame

from api.GameState import GameState
from api.Game import Game
from api.GameObject import GameObject
from api.EnemyManager import EnemyManager
from api.TextSprite import TextSprite

from game.Player import Player
from game.GameData import GameData

class LevelState(GameState):

    mPlayer = None
    mImgSpace = None

    mTextLives1 = None
    mTextLives2 = None
    mTextScore1 = None
    mTextScore2 = None

    def __init__(self):
        GameState.__init__(self)

        self.mImgSpace = None
        self.mPlayer = None

        self.mTextLives1 = None
        self.mTextLives2 = None
        self.mTextScore1 = None
        self.mTextScore2 = None

    def init(self):
        GameState.init(self)

        self.mImgSpace = pygame.image.load("assets/images/background.png")
        self.mImgSpace = self.mImgSpace.convert()

        Game.inst().setBackground(self.mImgSpace)

        self.mPlayer = Player()
        self.mPlayer.setXY(Game.SCREEN_WIDTH / 4 - self.mPlayer.getWidth() / 2,
                            Game.SCREEN_HEIGHT - self.mPlayer.getHeight() - 20)
        self.mPlayer.setBounds(0, 0, Game.SCREEN_WIDTH - self.mPlayer.getWidth(), Game.SCREEN_HEIGHT)

        self.mPlayer.setBoundAction(GameObject.STOP)

        GameData.inst().setScore(0)
        GameData.inst().setLives(3)

        self.mTextScore = TextSprite("SCORE: " + str(GameData.inst().getScore()), 20,
                                      "assets/fonts/days.otf")
        self.mTextLives = TextSprite("VIDAS: " + str(GameData.inst().getLives()), 20,
                                      "assets/fonts/days.otf")

        self.mTextScore.setXY(5, 5)

        self.mTextLives.setXY(5, Game.SCREEN_HEIGHT - 20 - 5)

    def update(self):
        GameState.update(self)

        self.mPlayer.update()

        if self.mPlayer.isGameOver():
            print('GG IZI')

        EnemyManager.inst().update()

        self.mTextScore.update()

        self.mTextLives.update()

    def render(self):
        GameState.render(self)

        screen = Game.inst().getScreen()
        self.mPlayer.render(screen)

        EnemyManager.inst().render(screen)

        self.mTextScore.setText("SCORE: " + str(GameData.inst().getScore()))
        self.mTextLives.setText("VIDAS: " + str(GameData.inst().getLives()))

        self.mTextScore.render(screen)
        self.mTextLives.render(screen)

    def drawText(self, aScreen, aX, aY, aMsg, aSize, aColor = (0, 0, 0)):
        font = pygame.font.Font("assets/fonts/days.otf", aSize)
        imgTxt = font.render(aMsg, True, aColor)
        aScreen.blit(imgTxt, (aX, aY))

    def destroy(self):
        GameState.destroy(self)

        self.mPlayer.destroy()
        self.mPlayer = None

        self.mTextScore.destroy()
        self.mTextLives.destroy()

        self.mImgSpace = None
        EnemyManager.inst().destroy()
        GameData.inst().destroy()