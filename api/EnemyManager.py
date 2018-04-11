# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------------
# Clase EnemyManager.
# Clase para manejar los enemigos del juego.
#
# Autor: Batovi Games Studio - 2013
# Proyecto: Hacete tu Videojuego.
#           Plan CEIBAL, Uruguay.
# Licencia: Creative Commons. BY-SA.
# --------------------------------------------------------------------------------

import pygame
from api.Manager import *


class EnemyManager(Manager):
    mInstance = None
    mInitialized = False

    def __new__(self, *args, **kargs):
        if (EnemyManager.mInstance is None):
            EnemyManager.mInstance = object.__new__(self, *args, **kargs)
            self.init(EnemyManager.mInstance)
        else:
            print("Cuidado: EnemyManager(): No se debería instanciar más de una vez esta clase. Usar EnemyManager.inst().")
        return self.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance

    def init(self):
        if (EnemyManager.mInitialized):
            return
        EnemyManager.mInitialized = True

        Manager.__init__(self)

    def update(self):
        Manager.update(self)

    def render(self, aScreen):
        Manager.render(self, aScreen)

    def addEnemy(self, aEnemy):
        Manager.add(self, aEnemy)

    def getLength(self):
        return len(self.mArray)

    def destroy(self):
        Manager.destroy(self)

        EnemyManager.mInstance = None
