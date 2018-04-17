import pygame
from api.AnimatedSprite import AnimatedSprite
from api.Keyboard import Keyboard
from api.GameObject import GameObject
from api.GameConstants import GameConstants
from api.AudioManager import AudioManager
from api.Mouse import Mouse
from api.Rectangle import Rectangle

from game.managers.AstralManager import AstralManager 
from game.GameData import GameData
from game.entities.Planet import Planet
from game.entities.Star import Star


class Player(AnimatedSprite):
    TYPE_PLAYER_1 = 0

    NORMAL = 0
    DYING = 1
    DEFENDING = 2
    GAME_OVER = 3

    # Tiempo que duran los estados
    TIME_DYING = 30
    TIME_START = 60
    SCORE_LOSS_PER_SECOND_DEFENDING = 5

    def __init__(self):
        AnimatedSprite.__init__(self)

        self.mFrames = []
        self.rockFrames = []
        i = 0
        while i <= 7:
            tmpImg = pygame.image.load(
                "assets\\images\\player0" + str(i) + ".png").convert_alpha()
            self.mFrames.append(tmpImg)
            i += 1

        i = 0
        while i <= 7:
            tmpImg = pygame.image.load(
                "assets\\images\\rock-player0" + str(i) + ".png").convert_alpha()
            self.rockFrames.append(tmpImg)
            i += 1

        self.setImage(self.mFrames[0])
        self.initAnimation(self.mFrames, 0, 4, True)
        self.setState(Player.NORMAL)
        self.mouth = Rectangle(self.right() - 30, self.top(), 30, self.getHeight())
        self.defendingTimer = 0

    def update(self):
        self.mouth.setX(self.right() - self.mouth.getWidth())
        self.mouth.setY(self.top())
        self.mouth.setHeight(self.getHeight())


        if self.getState() == Player.NORMAL:

            astral = AstralManager.inst().collides(self.mouth)
            if astral:
                self.collideAction(astral)
                self.setScale(self.mScale + 0.01)

            self.move()

            if Mouse.inst().leftPressed() and GameData.inst().getScore() >= Player.SCORE_LOSS_PER_SECOND_DEFENDING:
                self.setState(Player.DEFENDING)


        elif self.getState() == Player.DEFENDING:
            if not Mouse.inst().leftPressed() or GameData.inst().getScore() < Player.SCORE_LOSS_PER_SECOND_DEFENDING:
                self.setState(Player.NORMAL)
            
            self.defendingTimer += 1

            # TODO: Magic number 30fps == 1 second
            if self.defendingTimer > 30:
                GameData.inst().substractScore(Player.SCORE_LOSS_PER_SECOND_DEFENDING)
                self.defendingTimer = 0
            

        elif self.getState() == Player.DYING:
            if self.getTimeState() > Player.TIME_DYING:
                self.setState(Player.GAME_OVER)
                return

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

        AnimatedSprite.render(self, aScreen)

    def setState(self, aState):
        AnimatedSprite.setState(self, aState)

        self.setVisible(True)

        if self.getState() == Player.DYING:
            self.initAnimation(self.mFrames, 0, 0, False)

        elif self.getState() == Player.NORMAL:
            self.initAnimation(self.mFrames, 0, 2, True)

        elif self.getState() == Player.DEFENDING:
            self.defendingTimer = 0
            self.initAnimation(self.rockFrames, self.getCurrentFrame(), 0, False)
            self.gotoAndStop(self.getCurrentFrame())
            self.stopMove()

        elif self.getState() == Player.GAME_OVER:
            self.setVisible(False)

    def isGameOver(self):
        return self.getState() == Player.GAME_OVER

    def collideAction(self, astral):
        if type(astral) == Planet:
            GameData.inst().addScore(astral.getScore())
            astral.die()
        elif type(astral) == Star:
            self.setState(Player.GAME_OVER)

    def destroy(self):
        AnimatedSprite.destroy(self)

        i = len(self.mFrames)
        while i > 0:
            self.mFrames[i-1] = None
            self.mFrames.pop(i-1)
            i -= 1
