import pygame


class Manager(object):
    def __init__(self):

        self.mArray = []

    def update(self):
        for e in self.mArray:
            e.update()

        i = len(self.mArray)
        while i > 0:
            if self.mArray[i - 1].isDead():
                self.mArray[i - 1].destroy()
                self.mArray.pop(i - 1)
            i = i - 1

    def render(self, aScreen):
        for e in self.mArray:
            e.render(aScreen)

    def add(self, aElement):
        self.mArray.append(aElement)

    def collides(self, aSprite):
        i = 0

        while i < len(self.mArray):
            if self.mArray[i].collides(aSprite):
                return self.mArray[i]
            i += 1
        return None

    def destroy(self):
        i = len(self.mArray)
        while i > 0:
            self.mArray[i - 1].destroy()
            self.mArray.pop(i - 1)
            i = i - 1