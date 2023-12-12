# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# Clase CCuadrado.
# Simple cuadrado que se mueve por la pantalla chequeando los bordes.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
# --------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase CGameObject.
from api.CGameObject import *

# La clase CCuadrado hereda de CGameObject.
class CCuadrado(CGameObject):

    # ----------------------------------------------------------------
    # Constructor.
    # Parámetros:
    # aWidth: Ancho del cuadrado.
    # aHeight: Alto del cuadrado.
    # aColor: Color del cuadrado en formato RGB (r,g,b).
    # ----------------------------------------------------------------
    def __init__(self, aWidth, aHeight, aColor):

        # Invocar al constructor de la clase base.
        CGameObject.__init__(self)

        # Color.
        self.mColor = aColor

        # Crear la superficie y llenarla con el color.
        self.mImg = pygame.Surface((aWidth, aHeight))
        self.mImg = self.mImg.convert()
        self.mImg.fill(aColor)

        # Guardar el ancho y el alto.
        self.mWidth = self.mImg.get_width()
        self.mHeight = self.mImg.get_height()

    # Mover el objeto.
    def update(self):

        # Invocar a update() de la clase base para el movimiento.
        CGameObject.update(self)

    # Dibuja el objeto en la pantalla.
    # Parámetros:
    # aScreen: La superficie de la pantalla en donde dibujar.
    def render(self, aScreen):

        aScreen.blit(self.mImg, (self.mX, self.mY))

    # Liberar lo que haya creado el objeto.
    def destroy(self):

        # Invocar a destroy() de la clase base.
        CGameObject.destroy(self)
        self.mImg = None