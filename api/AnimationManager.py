import pygame

class AnimationManager():
	mInstance = None
	mInitialized = False
	mDictionary = dict()

	def __new__(self, *args, **kargs):
		if (AnimationManager.mInstance is None):
			AnimationManager.mInstance = object.__new__(self, *args, **kargs)
			self.init(AnimationManager.mInstance)
		else:
			print("Cuidado: AnimationManager(): No se debería instanciar más de una vez esta clase. Usar AnimationManager.inst().")
		return self.mInstance

	@classmethod
	def inst(cls):
		if (not cls.mInstance):
			return cls()
		return cls.mInstance

	def init(self):
		if (AnimationManager.mInitialized):
			return
		AnimationManager.mInitialized = True

	def setAnimation(self, aKey, aFrames):
		AnimationManager.inst().mDictionary[aKey] = aFrames

	def getAnimation(self, aKey):
		return AnimationManager.inst().mDictionary[aKey] if aKey in AnimationManager.inst().mDictionary else False

	def loadAnimation(self, aKey, aFileName, aFrameQuantity, aScale=None):
		if AnimationManager.inst().getAnimation(aKey):
			return AnimationManager.inst().getAnimation(aKey)

		frames = []
		i = 0
		while i < aFrameQuantity:
			img = pygame.image.load(
				aFileName + str(i) + ".png").convert_alpha()
			
			if not aScale is None:
				img = pygame.transform.scale(
					img, (int(img.get_width() * aScale), int(img.get_height() * aScale)))
			frames.append(img)
			i += 1
		
		AnimationManager.inst().setAnimation(aKey, frames)
		return AnimationManager.inst().getAnimation(aKey)

	def destroy(self):
		AnimationManager.mInstance = None
		AnimationManager.mDictionary = None
