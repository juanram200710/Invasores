# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CSprite.
# Simple sprite con una imagen. Hereda de CGameObject.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase CGameObject.
from api.CGameObject import *

class CSprite(CGameObject):

    # Constructor:
    def __init__(self):

        CGameObject.__init__(self)

        # Score del sprite
        self.mScore = 0
        
        # Imagen (superficie) del sprite.
        # Usar setImage() en la clase superior para establecer una imagen.
        self.mImg = None

        # Ancho y alto de la imagen. La función setImage() los actualiza.
        self.mWidth = 0
        self.mHeight = 0

        # Indica si el sprite es visible o no.
        self.mVisible = True

    # Establecer la imagen del sprite.
    def setImage(self, aImg):

        # Establecer la imagen.
        self.mImg = aImg

        # Guardar el ancho y el alto.
        self.mWidth = self.mImg.get_width()
        self.mHeight = self.mImg.get_height()

    # Mover el objeto.
    def update(self):

        # Invocar a update() de la clase base para el movimiento.
        CGameObject.update(self)

    # Dibuja el objeto en la pantalla.
    # Parámetros: La superficie de la pantalla donde dibujar la imagen.
    def render(self, aScreen):

        if (self.mImg != None):
            if self.mVisible:
                aScreen.blit(self.mImg, (self.getX(), self.getY()))

    # Obtener el ancho del sprite.
    def getWidth(self):

        return self.mWidth

    # Obtener el alto del sprite.
    def getHeight(self):

        return self.mHeight

    # Liberar lo que haya creado el objeto.
    def destroy(self):
        CGameObject.destroy(self)
        self.mImg = None

    # Función para detectar colisión contra otro sprite.
    def collides(self, aSprite):
        x1 = self.getX()
        y1 = self.getY()
        w1 = self.getWidth()
        h1 = self.getHeight()
        x2 = aSprite.getX()
        y2 = aSprite.getY()
        w2 = aSprite.getWidth()
        h2 = aSprite.getHeight()

        if ((((x1 + w1) > x2) and (x1 < (x2 + w2))) and (((y1 + h1) > y2) and (y1 < (y2 + h2)))):
            return True
        else:
            return False

    # Establece si el sprite es visible o no.
    # Parámetro: True para que se dibuje, False para que no se dibuje.
    def setVisible(self, aVisible):
        self.mVisible = aVisible

    # Retorna True si el sprite es visible y False si no lo es.
    def isVisible(self):
        return self.mVisible
    
    # Establecer el score del sprite
    def setScore(self, aScore):
        self.mScore = aScore

    # Obtener el score del sprite
    def getScore(self):
        return self.mScore
    
        
