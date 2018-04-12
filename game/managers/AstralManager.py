import pygame
import random
from api.Manager import *
from api.GameConstants import GameConstants

from game.entities.Planet import Planet

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
        planets = random.randint(3, 6)

        for x in range(0, planets):
            planet = Planet()
            planet.setXY(
                planet.getWidth() * 3 * x + GameConstants.SCREEN_WIDTH,
                random.randint(0, GameConstants.SCREEN_HEIGHT - planet.getHeight())
            )
            self.add(planet)
        
        
        
