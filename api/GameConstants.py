import pygame
class GameConstants(object):

     mInstance = None
     mInitialized = False
     SCREEN_WIDTH = 1280
     SCREEN_HEIGHT = 720

     def __new__(self, *args, **kargs):
         if (GameConstants.mInstance is None):
             GameConstants.mInstance = object.__new__(self, *args, **kargs)
             self.init(GameConstants.mInstance)
         else:
             print ("Cuidado: GameConstants(): No se debería instanciar más de una vez esta clase. Usar GameConstants.inst().")
         return self.mInstance

     @classmethod
     def inst(cls):
        if (not cls.mInstance):
            return cls()

        return cls.mInstance

     def init(self):
         if (GameConstants.mInitialized):
            return

         GameConstants.mInitialized = True

     def destroy(self):
        GameConstants.mInstance = None