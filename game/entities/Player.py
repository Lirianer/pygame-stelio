import pygame
from api.AnimatedSprite import AnimatedSprite
from api.Keyboard import Keyboard
from api.GameObject import GameObject
from api.GameConstants import GameConstants
from api.EnemyManager import EnemyManager
from api.AudioManager import AudioManager
from api.Mouse import Mouse

from game.GameData import GameData


class Player(AnimatedSprite):
    TYPE_PLAYER_1 = 0

    NORMAL = 0
    DYING = 1
    EXPLODING = 2
    START = 3
    GAME_OVER = 4

    # Tiempo que duran los estados
    TIME_DYING = 30
    TIME_EXPLODING = 30
    TIME_START = 60

    def __init__(self):
        AnimatedSprite.__init__(self)

        name = "assets\\images\\player0"

        self.mFrames = []
        i = 0
        while i <= 0:
            tmpImg = pygame.image.load(name + str(i) + ".png").convert_alpha()
            self.mFrames.append(tmpImg)
            i += 1

        self.setImage(self.mFrames[0])
        self.setState(Player.NORMAL)

    def update(self):
        if self.getState() == Player.NORMAL:
            enemy = EnemyManager.inst().collides(self)
            if enemy:
                self.setState(Player.DYING)
                return

            self.move()

        elif self.getState() == Player.DYING:
            if self.getTimeState() > Player.TIME_DYING:
                self.setState(Player.EXPLODING)
                return
        elif self.getState() == Player.EXPLODING:
            if self.getTimeState() > Player.TIME_EXPLODING:
                if self.isEnded():
                    if self.isPlayerOne():
                        if(GameData.inst().getLives1() == 0):
                            self.setState(Player.GAME_OVER)
                        else:
                            GameData.inst().addLives1(-1)
                            self.setState(Player.START)
                    else:
                        if(GameData.inst().getLives2() == 0):
                            self.setState(Player.GAME_OVER)
                        else:
                            GameData.inst().addLives2(-1)
                            self.setState(Player.START)
                return
        elif self.getState() == Player.START:
            if self.getTimeState() > Player.TIME_START:
                self.setState(Player.NORMAL)
                return
            self.move()

        elif self.getState() == Player.GAME_OVER:
            return

        AnimatedSprite.update(self)

    def move(self):
        mouse = Mouse.inst()

        velX = 0
        velY = 0

        if(self.right() + 5 < mouse.getX()):
            velX = 8
        elif(self.right() - 5 > mouse.getX()):
            velX = -8
        
        if(self.top() > mouse.getY()):
            velY = -8
        elif(self.bottom() < mouse.getY()):
            velY = 8

        self.setVelX(velX)
        self.setVelY(velY)

    def render(self, aScreen):
        if self.getState() == Player.GAME_OVER:
            return

        if self.getState() == Player.DYING:
            if self.getTimeState() % 2 == 0:
                self.setVisible(True)
            else:
                self.setVisible(False)
        elif self.getState() == Player.START:
            if self.getTimeState() % 6 == 0:
                self.setVisible(True)
            else:
                self.setVisible(False)

        AnimatedSprite.render(self, aScreen)

    def setState(self, aState):
        AnimatedSprite.setState(self, aState)

        self.setVisible(True)

        if self.getState() == Player.DYING:
            self.stopMove()
            self.initAnimation(self.mFrames, 0, 0, False)
            self.gotoAndStop(0)
        elif self.getState() == Player.START:
            self.initAnimation(self.mFrames, 0, 0, False)
            self.gotoAndStop(0)
        elif self.getState() == Player.EXPLODING:
            print('exploding')

        elif self.getState() == Player.NORMAL:
            self.initAnimation(self.mFrames, 0, 0, False)
            self.gotoAndStop(0)

        elif self.getState() == Player.GAME_OVER:
            self.setVisible(False)

    def isPlayerOne(self):
        return self.mType == Player.TYPE_PLAYER_1

    def isGameOver(self):
        return self.getState() == Player.GAME_OVER

    def destroy(self):
        AnimatedSprite.destroy(self)

        i = len(self.mFrames)
        while i > 0:
            self.mFrames[i-1] = None
            self.mFrames.pop(i-1)
            i -= 1
