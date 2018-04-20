import pygame
from api.Math import Math
from api.Manager import *
from api.GameConstants import GameConstants

from game.GameData import GameData
from game.entities.Planet import Planet
from game.entities.Star import Star

class AstralManager(Manager):
    mInstance = None
    mInitialized = False

    def __new__(self, *args, **kargs):
        if (AstralManager.mInstance is None):
            AstralManager.mInstance = object.__new__(self, *args, **kargs)
            self.init(AstralManager.mInstance)
        else:
            print("Cuidado: AstralManager(): No se debería instanciar más de una vez esta clase. Usar AstralManager.inst().")
        return self.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance

    def init(self):
        if (AstralManager.mInitialized):
            return
        AstralManager.mInitialized = True

        Manager.__init__(self)

    def update(self):
        Manager.update(self)

        if self.inst().getLength() == 0:
            self.inst().spawnSystem()

    def render(self, aScreen):
        Manager.render(self, aScreen)

    def add(self, aElement):
        Manager.add(self, aElement)

    def getLength(self):
        return len(self.mArray)

    def destroy(self):
        Manager.destroy(self)

        AstralManager.mInstance = None

    def spawnSystem(self):
        planets = Math.randomIntBetween(3, 6)

        for x in range(0, planets):

            planetType = Planet.TYPE_PLANET
            if Math.randomIntBetween(1, 3) == 1:
                planetType = Planet.TYPE_GAS

            planet = Planet(planetType)
            planet.setXY(
                planet.getWidth() * 3 * x + GameConstants.SCREEN_WIDTH,
                Math.randomIntBetween(0, GameConstants.SCREEN_HEIGHT - planet.getHeight())
            )
            planet.setVelX(-Math.clamp((20/10000 * GameData.inst().getHighestReached() + 10),
                                    GameConstants.MAX_ASTRAL_SPEED, GameConstants.MIN_ASTRAL_SPEED))
            self.add(planet)

        lastPlanet = self.mArray[len(self.mArray) - 1]
        star = Star()
        star.setXY(
            lastPlanet.getX() + lastPlanet.getWidth() + lastPlanet.getWidth() * Math.randomIntBetween(3, 8),
            Math.randomIntBetween(0, GameConstants.SCREEN_HEIGHT - star.getHeight())
        )
        star.setVelX(-Math.clamp((20/10000 * GameData.inst().getHighestReached() + 10),
                                 GameConstants.MAX_ASTRAL_SPEED, GameConstants.MIN_ASTRAL_SPEED))
        self.add(star)
        
        
        
