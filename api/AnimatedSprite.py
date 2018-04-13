import pygame
from api.Sprite import Sprite


class AnimatedSprite(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self.mTimeFrame = 0
        self.mDelay = 0

        self.mFrame = None
        self.mCurrentFrame = 0

        self.mIsLoop = True
        self.mEnded = False


    def initAnimation(self, aFramesArray, aStartFrame, aDelay, aIsLoop):
        self.mFrame = aFramesArray
        self.mCurrentFrame = aStartFrame
        self.mTimeFrame = 0
        self.mDelay = aDelay
        self.mIsLoop = aIsLoop
        self.mEnded = False

        self.setImage(self.mFrame[self.mCurrentFrame])

    def update(self):
        Sprite.update(self)

        self.mTimeFrame += 1

        if(self.mTimeFrame > self.mDelay):
            self.mTimeFrame = 0
            if not self.mEnded:
                self.mCurrentFrame += 1
                if self.mCurrentFrame >= len(self.mFrame):
                    if self.mIsLoop:
                        self.mCurrentFrame = 0
                    else:
                        self.mCurrentFrame = len(self.mFrame) - 1
                        self.mEnded = True

        self.setImage(self.mFrame[self.mCurrentFrame])

    def render(self, aScreen):
        Sprite.render(self, aScreen)

    def isEnded(self):
        return self.mEnded

    def gotoAndStop(self, aFrame):
        if aFrame >= 0 and aFrame <= len(self.mFrame) - 1:
            self.mCurrentFrame = aFrame
            self.setImage(self.mFrame[self.mCurrentFrame])
            self.mEnded = True

    def gotoAndPlay(self, aFrame):
        if aFrame >= 0 and aFrame <= len(self.mFrame) - 1:
            self.mCurrentFrame = aFrame
            self.setImage(self.mFrame[self.mCurrentFrame])
            self.mEnded = False
            self.mTimeFrame = 0

    def getCurrentFrame(self):
        return self.mCurrentFrame

    def destroy(self):
        Sprite.destroy(self)
        i = len(self.mFrame)
        while i > 0:
            self.mFrame[i - 1] = None
            self.mFrame.pop(i-1)
            i -= 1