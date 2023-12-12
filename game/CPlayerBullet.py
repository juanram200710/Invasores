# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CPlayerBullet.
# Balas del jugador.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase CSprite.
from api.CSprite import *

# Importar el manager de enemigos para detectar colisiones.
from game.CEnemyManager import *

# Importar la clase para guardar los datos
from game.CGameData import *

# La clase CPlayerBullet hereda de CSprite.
class CPlayerBullet(CSprite):

    # Constructor.
    def __init__(self, aPlayer):
        CSprite.__init__(self)

        img = pygame.image.load("assets/images/player_bullet.png")
        img = img.convert_alpha()
        self.setImage(img)

        # Guardar la referencia a quién disparó la bala
        self.mPlayer = aPlayer

    # Mover el objeto.
    def update(self):

        CSprite.update(self)

        # Detectar choque contra los enemigos.
        # Si la bala choca un enemigo, mueren ambos.
        enemy = CEnemyManager.inst().collides(self)
        if enemy != None:
            if enemy.isStateNormal():
                print("*****COLISION ENTRE BALA DEL JUGADOR Y ENEMIGO")
                enemy.hit()
                self.die()

                if self.mPlayer.isPlayerOne():
                    CGameData.inst().addScore1(enemy.getScore())
                else:
                    CGameData.inst().addScore2(enemy.getScore())
                        

    # Dibuja el objeto en la pantalla.
    # Parámetros:
    # aScreen: La superficie de la pantalla en donde dibujar.
    def render(self, aScreen):

        CSprite.render(self, aScreen)

    # Liberar lo que haya creado el objeto.
    def destroy(self):
        # Invocar la función para decrementar la cuenta de balas vivas.
        self.mPlayer.bulletDestroyed()

        CSprite.destroy(self)  
