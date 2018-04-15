import pygame

from api.GameState import GameState
from api.Game import Game
from api.GameObject import GameObject
from api.EnemyManager import EnemyManager
from api.TextSprite import TextSprite

from game.entities.Player import Player
from game.GameData import GameData
from game.managers.AstralManager import AstralManager
from game.MousePointer import MousePointer

from game.InfiniteBackground import InfiniteBackground

class LevelState(GameState):

    mPlayer = None
    mImgSpace = None
    cursor = None

    mTextLives1 = None
    mTextLives2 = None
    mTextScore1 = None
    mTextScore2 = None

    def __init__(self):
        GameState.__init__(self)

        self.mImgSpace = None
        self.mPlayer = None
        self.cursor = None

        self.mTextScore1 = None

    def init(self):
        GameState.init(self)

        self.background = InfiniteBackground()

        self.cursor = MousePointer()
        self.mPlayer = Player()
        self.mPlayer.setXY(Game.SCREEN_WIDTH / 4 - self.mPlayer.getWidth() / 2,
                            Game.SCREEN_HEIGHT - self.mPlayer.getHeight() - 20)
        self.mPlayer.setBounds(0, 0, Game.SCREEN_WIDTH - self.mPlayer.getWidth(), Game.SCREEN_HEIGHT)

        self.mPlayer.setBoundAction(GameObject.STOP)

        GameData.inst().setScore(0)

        self.mTextScore = TextSprite("SCORE: " + str(GameData.inst().getScore()), 20,
                                      "assets/fonts/days.otf")

        self.mTextScore.setXY(5, 5)
        
        AstralManager.inst().spawnSystem()

    def update(self):
        GameState.update(self)

        self.cursor.update()
        self.background.update()

        self.mPlayer.update()

        if self.mPlayer.isGameOver():
            print('PERDISTE')

        AstralManager.inst().update()

        self.mTextScore.update()

    def render(self):
        GameState.render(self)
        screen = Game.inst().getScreen()

        self.background.render(screen)

        AstralManager.inst().render(screen)
        self.mPlayer.render(screen)

        self.cursor.render(screen)


        self.mTextScore.setText("SCORE: " + str(GameData.inst().getScore()))
        self.mTextScore.render(screen)

    def drawText(self, aScreen, aX, aY, aMsg, aSize, aColor = (0, 0, 0)):
        font = pygame.font.Font("assets/fonts/days.otf", aSize)
        imgTxt = font.render(aMsg, True, aColor)
        aScreen.blit(imgTxt, (aX, aY))

    def destroy(self):
        GameState.destroy(self)

        self.cursor.destroy()

        self.mPlayer.destroy()
        self.mPlayer = None

        self.mTextScore.destroy()

        self.background.destroy()
        EnemyManager.inst().destroy()
        GameData.inst().destroy()