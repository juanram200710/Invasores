# *- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CFlame
# Fuego de la naves del jugador.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

import pygame

from api.CAnimatedSprite import *

class CFlame(CAnimatedSprite):

    def __init__(self): 

        CAnimatedSprite.__init__(self)

        self.mFrames = []
        i = 0
        while i <= 2:
            num = "0" + str(i)
            tmpImg = pygame.image.load("assets/images/fire" + num + ".png")
            tmpImg = tmpImg.convert_alpha()
            self.mFrames.append(tmpImg)
            i = i + 1

        self.initAnimation(self.mFrames, 0, 2, True)

    def update(self):
        CAnimatedSprite.update(self)

    def render(self, aScreen):
        CAnimatedSprite.render(self, aScreen) 

    def destroy(self):
        CAnimatedSprite.destroy(self)

        i = len(self.mFrames)
        while i > 0:
            self.mFrames[i - 1] = None
            self.mFrames.pop(i - 1)
            i = i - 1
                           