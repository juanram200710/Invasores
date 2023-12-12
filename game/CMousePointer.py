# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# Clase CMousePointer
# Sprite del puntero del mouse.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
# --------------------------------------------------------------------

# Importar Pygame
import pygame

# Importar la clase CSprite
from api.CSprite import *

# Importar la clase CMouse
from api.CMouse import *

class CMousePointer(CSprite):

    def __init__(self):
        CSprite.__init__(self)

        img = pygame.image.load("assets/images/cursor.png")
        img = img.convert_alpha()
        self.setImage(img)

    def update(self):
        CSprite.update(self)

        # Colocar el sprite en donde está el mouse
        self.setXY(CMouse.inst().getX(), CMouse.inst().getY())

    def render(self, aScreen):
        CSprite.render(self, aScreen)

    def destroy(self):
        CSprite.destroy(self)
        
                    