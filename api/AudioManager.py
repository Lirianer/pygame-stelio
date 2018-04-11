import pygame

class AudioManager(object):

    mInstance = None
    mInitialized = False

    mChannels = 8

    def __new__(cls, *args, **kwargs):
        if AudioManager.mInstance is None:
            AudioManager.mInstance = object.__new__(cls, *args, **kwargs)
            cls.init(AudioManager.mInstance)
        else:
            print("Cuidado: AudioManager(): No se deberia instanciar mas de una vez esta clase. Usar AudioManager.init()")

        return AudioManager.mInstance

    @classmethod
    def inst(cls):
        if not cls.mInstance:
            return cls()
        return cls.mInstance

    def init(self):
        if AudioManager.mInitialized:
            return

        AudioManager.mInitialized = True
        AudioManager.mChannels = pygame.mixer.get_num_channels()

    def play(self, aSound):
        AudioManager.inst().get_channel().play(aSound)

    def get_channel(self):
        c = pygame.mixer.find_channel(True)
        while c is None:
            AudioManager.mChannels += 1
            pygame.mixer.set_num_channels(AudioManager.mChannels)
            c = pygame.mixer.find_channel()
        return c

    def destroy(self):
        AudioManager.mInstance = None
