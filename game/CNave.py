# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# Clase CNave.
# Nave enemiga que se mueve por la pantalla chequeando los bordes.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
# --------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase para sprites animados.
from api.CAnimatedSprite import *

# Importar las clases necesarias para disparar.
import random
from game.CEnemyBullet import * 
from api.CGameConstants import *
from game.CEnemyManager import *

# Importar la clase que maneja el audio
from api.CAudioManager import *

# La clase CNave hereda de CAnimatedSprite.
class CNave(CAnimatedSprite):

    # Tipos de naves.
    TYPE_PLATINUM = 0
    TYPE_GOLD = 1
    TYPE_RED = 2
    TYPE_GREEN = 4
    TYPE_CYAN = 3

    # Máquina de estados.
    NORMAL = 0
    EXPLODING = 1

    # ----------------------------------------------------------------
    # Constructor. Recibe el tipo de nave (TYPE_PLATINUM o TYPE_GOLD).
    # ----------------------------------------------------------------
    def __init__(self, aType):
        CAnimatedSprite.__init__(self)

        # Segun el tipo de la nave, la imagen que se carga.
        self.mType = aType

        if self.mType == CNave.TYPE_PLATINUM:
            imgFile = "assets/images/grey_ufo_0"
            self.setScore(25)
        elif self.mType == CNave.TYPE_GOLD:
            imgFile = "assets/images/yellow_ufo_0"
            self.setScore(20)
        elif self.mType == CNave.TYPE_RED:
            imgFile = "assets/images/red_ufo_0"
            self.setScore(15)
        elif self.mType == CNave.TYPE_CYAN:
            imgFile = "assets/images/cyan_ufo_0"
            self.setScore(10)
        elif self.mType == CNave.TYPE_GREEN:
            imgFile = "assets/images/green_ufo_0"
            self.setScore(5)

        # Cargar la secuencia de imágenes.
        self.mFramesNormal = []
        i = 0
        while (i <= 8):
            tmpImg = pygame.image.load(imgFile + str(i) + ".png")
            tmpImg = tmpImg.convert_alpha()
            self.mFramesNormal.append(tmpImg)
            i = i + 1

        # Cargar la secuencia de imágenes de la explosion.
        self.mFramesExplosion = []
        i = 0
        while (i <= 9):
            num = "0" + str(i)
            tmpImg = pygame.image.load("assets/images/explosion" + num + ".png")
            tmpImg = tmpImg.convert_alpha()
            self.mFramesExplosion.append(tmpImg)
            i = i + 1

        # Estado inicial.
        self.setState(CNave.NORMAL)

    # Mover el objeto.
    def update(self):

        # Invocar update() de CAnimatedSprite.
        CAnimatedSprite.update(self)

        if self.getState() == CNave.NORMAL:
            self.controlFire()

        elif self.getState() == CNave.EXPLODING:
            self.stopMove()
            
            if self.isEnded():
                self.die()
                return

    # Dibuja el objeto en la pantalla.
    # Parámetros:
    # aScreen: La superficie de la pantalla en donde dibujar.
    def render(self, aScreen):

        # Invocar render() de CAnimatedSprite.
        CAnimatedSprite.render(self, aScreen)

    # Liberar lo que haya creado el objeto.
    def destroy(self):

        # Invocar destroy() de CAnimatedSprite.
        CAnimatedSprite.destroy(self)

        # Eliminar todos los frames creados.
        i = len(self.mFramesNormal)
        while i > 0:
            self.mFramesNormal[i - 1] = None
            self.mFramesNormal.pop(i - 1)
            i = i - 1
        # Eliminar el array.
        self.mFramesNormal = None

        i = len(self.mFramesExplosion)
        while i > 0:
            self.mFramesExplosion[i - 1] = None
            self.mFramesExplosion.pop(i - 1)
            i = i - 1
        self.mFramesExplosion = None

    def setState(self, aState):
        CAnimatedSprite.setState(self, aState)

        if self.getState() == CNave.NORMAL:
            self.initAnimation(self.mFramesNormal, 0, 0, True)
        elif self.getState() == CNave.EXPLODING:
            self.initAnimation(self.mFramesExplosion, 0, 0, False)
            self.stopMove()

            # Ejecutar el sonido de la explosión
            CAudioManager.inst().play(CAudioManager.mSoundExplosionEnemy)
            
    # Invocada desde Bullet cuando la Nave es alcanzada por una bala.
    def hit(self):
        if self.getState() == CNave.NORMAL:
            self.setState(CNave.EXPLODING)
            print("NAVE EXPLOTA")

    def controlFire(self):
        # Ver si la nave dispara.
        if random.randrange(1, 500) == 1:
            b = CEnemyBullet()
            b.setXY(self.getX() + self.getWidth() / 2 - b.getWidth() / 2, self.getY() + self.getHeight())
            b.setVelX(0)
            b.setVelY(10)
            b.setBounds(0, 0, CGameConstants.SCREEN_WIDTH, CGameConstants.SCREEN_HEIGHT)
            b.setBoundAction(CGameObject.DIE)
            CEnemyManager.inst().add(b)

            # Ejecutar sonido del disparo
            CAudioManager.inst().play(CAudioManager.mSoundShootEnemy)

    # Retorna True si la nave está en estado normal.
    def isStateNormal(self):
        return self.getState() == CNave.NORMAL
    
    # Establecer si el enemigo puede disparar o no.
    def setCanShoot(self, aCanShoot):
        self.mCanShoot = aCanShoot

