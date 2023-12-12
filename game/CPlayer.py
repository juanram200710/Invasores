# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CPlayer.
# Nave que controla el jugador.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase CAnimatedSprite.
from api.CAnimatedSprite import *

# Importar la clase CKeyboard
from api.CKeyboard import *

# Importar el manager de balas.
from api.CBulletManager import *

# Importar la clase para la bala.
from game.CPlayerBullet import *

# Importar la clase CGameConstants
from api.CGameConstants import *

# Importar la clase del manager de audio
from api.CAudioManager import *

from game.CFlame import *

# La clase CPlayer hereda de CAnimatedSprite.
class CPlayer(CAnimatedSprite):

    # Tipos de jugador.
    TYPE_PLAYER_1 = 0
    TYPE_PLAYER_2 = 1

    # Máquina de estados.
    NORMAL = 0
    DYING = 1
    EXPLODING = 2
    START = 3
    GAME_OVER = 4

    # Tiempos que duran los estados.
    TIME_DYING = 60
    TIME_START = 120

    # Máxima cantidad de disparos a la vez.
    MAX_BULLETS = 1

    # ----------------------------------------------------------------
    # Constructor. Recibe el tipo de nave (TYPE_PLAYER_1 o TYPE_PLAYER_2).
    # ----------------------------------------------------------------
    def __init__(self, aType):

        # Invocar al constructor de CAnimatedSprite.
        CAnimatedSprite.__init__(self)

        # Segun el tipo de la nave, la imagen que se carga.
        self.mType = aType

        if self.mType == CPlayer.TYPE_PLAYER_1:
            imgFile = "assets/images/player0"
        elif self.mType == CPlayer.TYPE_PLAYER_2:
            imgFile = "assets/images/player1"

        self.mFrames = []
        i = 0
        while (i <= 2):
            tmpImg = pygame.image.load(imgFile + str(i) + ".png")
            tmpImg = tmpImg.convert_alpha()
            self.mFrames.append(tmpImg)
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

        # Cantidad de balas en el momento.
        self.mBulletCount = 0  

        # Crear la llama de la nave y posicionarla.
        self.mFlame = CFlame()
        self.setFlamePosition()  

        # Estado inicial.
        self.setState(CPlayer.NORMAL)

    # Mover el objeto.
    def update(self):

        # Invocar update() de CAnimatedSprite.
        CAnimatedSprite.update(self)

        # Luego de mover la nave, actualizar la llama
        self.mFlame.update()
        self.setFlamePosition()
        
        # Obtener el enemigo con el cual chocamos.
        enemy = CEnemyManager.inst().collides(self)

        # Si chocamos con un enemigo, el enemigo se muere.
        if enemy != None:
            enemy.hit()

        # Lógica del estado normal.
        if self.getState() == CPlayer.NORMAL:
            if enemy != None:
                self.setState(CPlayer.DYING)
                return
            self.move()

        # Lógica del estado muriendo.
        elif self.getState() == CPlayer.DYING:
            if (self.getTimeState() > CPlayer.TIME_DYING):
                self.setState(CPlayer.EXPLODING)
                return

        # Lógica del estado explotando.
        elif self.getState() == CPlayer.EXPLODING:
            if self.isEnded():
                # En este punto comienza una nueva vida
                if self.isPlayerOne():
                    if (CGameData.inst().getLives1() == 0):
                        print("Player 1 NO JUEGA MÁS")
                        self.setState(CPlayer.GAME_OVER)
                    else:
                        CGameData.inst().addLives1(-1)
                        if (CGameData.inst().getLives1() == 0):
                            print("Player 1 NO JUEGA MÁS")
                            self.setState(CPlayer.GAME_OVER) 
                        else:       
                            self.setState(CPlayer.START)
                else:
                    if (CGameData.inst().getLives2() == 0):
                        print("PLAYER 2 NO JUEGA MÁS")
                        self.setState(CPlayer.GAME_OVER)   
                    else:
                        CGameData.inst().addLives2(-1)
                        if (CGameData.inst().getLives2() == 0):
                            print("PLAYER 2 NO JUEGA MÁS")
                            self.setState(CPlayer.GAME_OVER)
                        else:    
                            self.setState(CPlayer.START)

                return

        # Lógica del estado start.
        elif self.getState() == CPlayer.START:
            if (self.getTimeState() > CPlayer.TIME_START):
                self.setState(CPlayer.NORMAL)
                return
            self.move()

        # En el estado GameOver no se hace nada
        elif self.getState() == CPlayer.GAME_OVER:
            return    


    # Dibuja el objeto en la pantalla.
    # Parámetros:
    # aScreen: La superficie de la pantalla en donde dibujar.
    def render(self, aScreen):

        # En el estado game over la nave no se dibuja
        if self.getState() == CPlayer.GAME_OVER:
            return

        # Poner visible o invisible según el caso.
        if self.getState() == CPlayer.DYING:
            if self.getTimeState() % 8 == 0:
                self.setVisible(True)
            else:
                self.setVisible(False)

        elif self.getState() == CPlayer.EXPLODING:
            pass

        elif self.getState() == CPlayer.START:
            if self.getTimeState() % 16 == 0:
                self.setVisible(True)
            else:
                self.setVisible(False)
        else:
            self.setVisible(True)

        CAnimatedSprite.render(self, aScreen)

        # Dibujar la llama
        self.mFlame.render(aScreen)

    # Liberar lo que haya creado el objeto.
    def destroy(self):

        # Invocar destroy() de CAnimatedSprite.
        CAnimatedSprite.destroy(self)

        i = len(self.mFrames)
        while i > 0:
            self.mFrames[i - 1] = None
            self.mFrames.pop(i - 1)
            i = i - 1
        mFrames = None

        i = len(self.mFramesExplosion)
        while i > 0:
            self.mFramesExplosion[i - 1] = None
            self.mFramesExplosion.pop(i - 1)
            i = i - 1
        self.mFramesExplosion = None

        if self.mFlame != None:
            self.mFlame.destroy()
            self.mFlame = None

    # Establece el estado actual e inicializa
    # las variables correspondientes al estado.
    def setState(self, aState):
        CAnimatedSprite.setState(self, aState)

        # Por defecto poner el sprite visible.
        self.setVisible(True)

        if self.getState() == CPlayer.NORMAL:
            self.initAnimation(self.mFrames, 0, 0, False)
            self.gotoAndStop(0)

        elif self.getState() == CPlayer.DYING:
            self.stopMove()
            self.initAnimation(self.mFrames, 0, 0, False)
            self.gotoAndStop(0)

            # Ejecutar sonido de morir
            CAudioManager.inst().play(CAudioManager.mSoundHitPlayer)

        elif self.getState() == CPlayer.EXPLODING:
            self.initAnimation(self.mFramesExplosion, 0, 2, False)

            # Ejecutar el sonido de la explosión
            CAudioManager.inst().play(CAudioManager.mSoundExplosionPlayer)

            self.mFlame.setVisible(False)

        elif self.getState() == CPlayer.START:
            self.initAnimation(self.mFrames, 0, 0, False)
            self.gotoAndStop(0)

        elif self.getState() == CPlayer.GAME_OVER:
            self.setVisible(False)    

    # Movimiento de la nave.
    def move(self):
        # Obtener los controles.
        if self.mType == CPlayer.TYPE_PLAYER_1:
            left = CKeyboard.inst().leftPressed()
            right = CKeyboard.inst().rightPressed()
            fire = CKeyboard.inst().fire()
        else:
            left = CKeyboard.inst().APressed()
            right = CKeyboard.inst().DPressed()
            fire = CKeyboard.inst().fire2()

        # Mover la nave según las teclas.
        if (not left and not right):
            self.setVelX(0)
            self.gotoAndStop(0)
        else:
            if left:
                self.setVelX(-4)
                self.gotoAndStop(1)
            elif right:
                self.setVelX(4)
                self.gotoAndStop(2)

        # Disparar.
        if fire:
            if self.mBulletCount < CPlayer.MAX_BULLETS:
                # Incrementar la cantidad de balas vivas.
                self.mBulletCount = self.mBulletCount + 1

                print("FIRE")
                b = CPlayerBullet(self)
                b.setXY(self.getX() + self.getWidth() / 2 - b.getWidth() / 2, self.getY())
                b.setVelX(0)
                b.setVelY(-10)
                b.setBounds(0, 0, CGameConstants.SCREEN_WIDTH, CGameConstants.SCREEN_HEIGHT)
                b.setBoundAction(CGameObject.DIE)
                CBulletManager.inst().add(b)

                # Sonido del disparo
                CAudioManager.inst().play(CAudioManager.mSoundShootPlayer)
            else:
                # Sonido de que no se puede dispara. 
                CAudioManager.inst().play(CAudioManager.mSoundCannotShoot)   

    # Retornar True si es el primer jugador. False si es el segundo
    def isPlayerOne(self):
        return self.mType == CPlayer.TYPE_PLAYER_1 

    # Retorna True si el jugador está en estado game over (si no tiene vidas)
    def isGameOver(self):
        return self.mState == CPlayer.GAME_OVER
    
    def bulletDestroyed(self):
        # Decrementar la cantidad de balas vivas.
        self.mBulletCount = self.mBulletCount - 1

    # Establecer si el sprite es visible o no.
    # Parámetro: True para que se dibuje, False para que no se dibuje
    def setVisible(self, aIsVisible):

        # Invocar destroy() de CAnimatedSprite()
        CAnimatedSprite.setVisible(self, aIsVisible)

        # Mostrar u ocultar la llama
        self.mFlame.setVisible(aIsVisible)
 
    # Posicionar la llama debajo de la nave.
    def setFlamePosition(self):
        self.mFlame.setX(self.getX() + self.getWidth() / 2 - self.mFlame.getWidth() / 2)
        self.mFlame.setY(self.getY() + self.getHeight())

           