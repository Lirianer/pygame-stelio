import pygame

class GameData(object):

    mInstance = None
    mInitialized = False

    mScore = 0

    mLives = 0

    def __new__(cls, *args, **kwargs):
        if GameData.mInstance is None:
            GameData.mInstance = object.__new__(cls, *args, **kwargs)
            cls.init(GameData.mInstance)
        else:
            print("Cuidado: GameData(): No se deberia instanciar mas de una vez esta clase. Usar GameData.inst().")
        return cls.mInstance

    @classmethod
    def inst(cls):
        if not cls.mInstance:
            return cls()
        return cls.mInstance

    def init(self):
        if GameData.mInitialized:
            return
        GameData.mInitialized = True

        GameData.mScore = 0
        GameData.mLives = 0

    def setScore(self, aScore):
        GameData.mScore = aScore
        self.controlScores()

    def addScore(self, aScore):
        GameData.mScore += aScore
        self.controlScores()

    def substractScore(self, aScore):
        GameData.mScore -= aScore
        self.controlScores()

    def controlScores(self):
        if GameData.mScore < 0:
            GameData.mScore = 0
        elif GameData.mScore > 99999:
            GameData.mScore = 99999

    def getScore(self):
        return GameData.mScore

    def setLives(self, aLives):
        GameData.mLives = aLives
        self.controlLives()

    def addLives(self, aLives):
        GameData.mLives += aLives
        self.controlLives()

    def controlLives(self):
        if GameData.mLives < 0:
            GameData.mLives = 0
        elif GameData.mLives > 9:
            GameData.mLives = 9

    def getLives(self):
        return GameData.mLives

    def destroy(self):
        GameData.mInstance = None