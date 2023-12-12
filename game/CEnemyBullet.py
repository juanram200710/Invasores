# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CEnemyBullet.
# Balas del enemigo.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Importar Pygame.
import pygame

# La clase CEnemyBullet hereda de CSprite
from api.CSprite import *

class CEnemyBullet(CSprite):

    # Constructor.
    def __init__(self):
        CSprite.__init__(self)

        img = pygame.image.load("assets/images/enemy_bullet.png")
        img = img.convert_alpha()
        self.setImage(img)

    # Mover el objeto.
    def update(self):

        CSprite.update(self)

    # Dibuja el objeto en la pantalla.
    # Parámetros:
    # aScreen: La superficie de la pantalla en donde dibujar.
    def render(self, aScreen):

        CSprite.render(self, aScreen)

    # Liberar lo que haya creado el objeto.
    def destroy(self):

        CSprite.destroy(self)

    # Invocada desde Bullet cuando la bala enemiga es alcanzada por una bala del jugador.
    def hit(self):
        self.die()
        print("COLISION BALA CONTRA BALA")

    # La bala enemigas no chocan contra las balas del jugador.
    def isStateNormal(self):
        return False
