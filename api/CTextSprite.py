# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CTextSprite.
# Sprite de texto. Hereda de CSprite.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

import pygame
from api.CSprite import *

class CTextSprite(CSprite):

    def __init__(self, aText = "", aFontSize = 10, aFontName = "", aColor = (0xFF, 0xFF, 0xFF)):

        CSprite.__init__(self)

        self.mText = aText
        self.mFontSize = aFontSize
        self.mFontName = aFontName
        self.mColor = aColor
        self.updateImage()

    # Función genérica para dibujar un texto en una superficie.
    # Parámetros: La pantalla donde dibujar, coordenadas (x, y),
    # texto, tamaño de la fuente y el color del texto.
    @classmethod
    def drawText(self, aScreen, aX, aY, aMsg, aFontName, aFontSize, aColor=(0, 0, 0)):
        font = pygame.font.Font(aFontName, aFontSize)
        imgTxt = font.render(aMsg, True, aColor)
        aScreen.blit(imgTxt, (aX, aY))

    def setText(self, aText):
        if self.mText != aText:
            self.mText = aText
            self.updateImage()

    def setFontName(self, aFontName):
        if self.mFontName != aFontName:
            self.mFontName = aFontName
            self.updateImage()

    def setColor(self, aColor):
        if self.mColor != aColor:
            self.mColor = aColor
            self.updateImage()

    def updateImage(self):
        if (self.mFontName == ""):
            font = pygame.font.SysFont("Comic Sans MS", self.mFontSize)
        else:
            font = pygame.font.Font(self.mFontName, self.mFontSize) 
        imgTxt = font.render(self.mText, True, self.mColor) 
        self.setImage(imgTxt)

    def update(self):
        CSprite.update(self)

    def render(self, aScreen):
        CSprite.render(self, aScreen)

    def destroy(self):
        CSprite.destroy(self)


            
                   
