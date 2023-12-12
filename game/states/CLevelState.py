# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CLevelState
# Nivel del juego. Es el juego en sí.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

import pygame
from api.CGameState import *
from api.CGame import *
from game.CNave import *
from game.CPlayer import *
from api.CGameObject import *
from game.CGameData import *
from api.CGameConstants import *
from api.CTextSprite import *
from game.CEnemyManager import *

class CLevelState(CGameState):

    mImgSpace = None
    mPlayer1 = None
    mPlayer2 = None

    mTextLives1 = None
    mTextLives2 = None
    mTextScore1 = None
    mTextScore2 = None

    # Máquina de estados
    PLAYING = 0
    INIT_LEVEL = 1
    TRANSITION = 2
    GAME_OVER = 3

    # Variables para el control de los mensajes y estados
    mLevel = 1
    TIME_SHOWING_LEVEL_TEXT = CGame.FPS * 2
    TIME_TRANSITION = CGame.FPS * 1
    TIME_SHOWING_GAME_OVER = CGame.FPS * 4
    mText = None
    
    # cantidad de jugadores
    mNumPlayers = 1

    def __init__(self, aNumPlayers):
        CGameState.__init__(self)
        print("LevelState Constructor")
        
        # establecer la cantidad de jugadores
        self.mNumPlayers = aNumPlayers

        self.mImgSpace = None
        self.mPlayer1 = None
        self.mPlayer2 = None

        self.mTextLives1 = None
        self.mTextScore1 = None
        if self.mNumPlayers == 2:
            
            self.mTextScore2 = None
            self.mTextLives2 = None

        # Comienzo del juego
        self.mLevel = 1
        self.mText = None
        
    # Función donde se inicializan los elementos necesarios del nivel
    def init(self):
        CGameState.init(self)
        print("LevelState init")

        # Cargar la imagen del fondo.
        self.mImgSpace = pygame.image.load("assets/images/space_640x360.jpg")
        self.mImgSpace = self.mImgSpace.convert()

        # Dibujar la imagen cargada en la imagen del background
        CGame.inst().setBackground(self.mImgSpace)  

        # Crear la formación inicial.
        self.initEnemies()

        # Crear el jugador 1
        self.mPlayer1 = CPlayer(CPlayer.TYPE_PLAYER_1) 
        self.mPlayer1.setXY(CGame.SCREEN_WIDTH / 4 - self.mPlayer1.getWidth() / 2, CGame.SCREEN_HEIGHT -self.mPlayer1.getHeight() - 20)
        self.mPlayer1.setBounds(0, 0, CGame.SCREEN_WIDTH - self.mPlayer1.getWidth(), CGame.SCREEN_HEIGHT) 
        self.mPlayer1.setBoundAction(CGameObject.STOP)

        # Crear el jugador 2
        if self.mNumPlayers == 2:
            self.mPlayer2 = CPlayer(CPlayer.TYPE_PLAYER_2) 
            self.mPlayer2.setXY(CGame.SCREEN_WIDTH / 4 * 3 - self.mPlayer2.getWidth() / 2, CGame.SCREEN_HEIGHT -self.mPlayer2.getHeight() - 20)
            self.mPlayer2.setBounds(0, 0, CGame.SCREEN_WIDTH - self.mPlayer2.getWidth(), CGame.SCREEN_HEIGHT)
            self.mPlayer2.setBoundAction(CGameObject.STOP)

        # Ejecutar la música de background (loop) del juego.
        pygame.mixer.music.load("assets/audio/music_game.ogg")
        pygame.mixer.music.play(-1)
        # Poner el volumen de la música
        pygame.mixer.music.set_volume(0.5) 

        # Inicializar los datos del juego
        CGameData.inst().setScore1(0)
        CGameData.inst().setLives1(3)
        CGameData.inst().setScore2(0)
        CGameData.inst().setLives2(3)

        self.mTextScore1 = CTextSprite("SCORE: " + str(CGameData.inst().getScore1()), 20, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
        self.mTextScore1.setXY(5, 5)
        self.mTextLives1 = CTextSprite("VIDAS: " + str(CGameData.inst().getLives1()), 20, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
        self.mTextLives1.setXY(5, CGame.SCREEN_HEIGHT - 20 -5)
        
        if self.mNumPlayers == 2:
            self.mTextScore2 = CTextSprite("SCORE: " + str(CGameData.inst().getScore2()), 20, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
            self.mTextScore2.setXY(500, 5)
            self.mTextLives2 = CTextSprite("VIDAS: " + str(CGameData.inst().getLives2()), 20, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
            self.mTextLives2.setXY(540, CGame.SCREEN_HEIGHT - 20 -5)

        # Ocultar el sprite del puntero del mouse.
        CGame.inst().showGamePointer(False)

        # Establecer el estado inicial
        self.setState(CLevelState.INIT_LEVEL)

    # Actualizar los objetos del nivel
    def update(self):
        CGameState.update(self)
        print("LevelState update()")

        # Actualizar los enemigos
        CEnemyManager.inst().update()

        # Mover las balas
        CBulletManager.inst().update()

        # Lógica de los jugadores
        self.mPlayer1.update()
        if self.mNumPlayers == 2:
            self.mPlayer2.update()

        print(self.getState)

        if self.getState() == CLevelState.INIT_LEVEL:
            if self.getTimeState() > CLevelState.TIME_SHOWING_LEVEL_TEXT:
                self.setState(CLevelState.PLAYING)
                return
            
        elif self.getState() == CLevelState.PLAYING:
            if (self.mNumPlayers == 1 and self.mPlayer1.isGameOver()) or (self.mNumPlayers == 2 and self.mPlayer1.isGameOver() and self.mPlayer2.isGameOver()):
                print("AMBOS JUGADORES MUEREN - LOSE CONDITION")
                self.setState(CLevelState.GAME_OVER)
                return
            
            if CEnemyManager.inst().getLength() == 0:
                print("TODOS LOS ENEMIGOS MUEREN -WIN CONDITION")
                self.setState(CLevelState.TRANSITION) 
                return

        elif self.getState() == CLevelState.GAME_OVER:
            if self.getTimeState() > CLevelState.TIME_SHOWING_GAME_OVER:
                from game.states.CMenuState import CMenuState
                nextState = CMenuState()
                CGame.inst().setState(nextState)
                return

        elif self.getState() == CLevelState.TRANSITION:
            if self.getTimeState() > CLevelState.TIME_TRANSITION:
                self.nextLevel()
                return
                       
        self.mTextScore1.update()
        self.mTextLives1.update()
        if self.mNumPlayers == 2:
            self.mTextScore2.update()
            self.mTextLives2.update()

        if self.mText != None:
            self.mText.update()    

        # Dibujar el frame del nivel.
    def render(self):
        CGameState.render(self)
        print("LevelState render()")

        # Obtener la referencia a la pantalla.
        screen = CGame.inst().getScreen()

        # Dibujar los enemigos
        CEnemyManager.inst().render(screen)

        # Dibujar las balas
        CBulletManager.inst().render(screen)

        # Dibujar los jugadores
        self.mPlayer1.render(screen)
        if self.mNumPlayers == 2:
            self.mPlayer2.render(screen)

        # Dibujar el texto del score y las vidas.

        self.mTextScore1.setText("SCORE: " + str(CGameData.inst().getScore1()))
        self.mTextLives1.setText("VIDAS: " + str(CGameData.inst().getLives1()))
        if self.mNumPlayers == 2:
            self.mTextScore2.setText("SCORE: " + str(CGameData.inst().getScore2()))
            self.mTextLives2.setText("VIDAS: " + str(CGameData.inst().getLives2()))

        self.mTextScore1.render(screen)
        self.mTextLives1.render(screen)
        if self.mNumPlayers == 2:
            self.mTextScore2.render(screen)
            self.mTextLives2.render(screen)

        if self.mText != None:
            self.mText.render(screen)
  
    # Destruir los objetos creados en el nivel.
    def destroy(self):
        CGameState.destroy(self)
        print("LevelState destroy()")

        # Destruir la nave de los jugadores.
        self.mPlayer1.destroy()
        self.mPlayer1 = None
        if self.mNumPlayers == 2:
            self.mPlayer2.destroy()
            self.mPlayer2 = None

        self.mImgSpace = None

        # Destruir las balas
        CBulletManager.inst().destroy()

        # Destruir los enemigos
        CEnemyManager.inst().destroy()

        self.mTextScore1.destroy()
        self.mTextScore1 = None
        self.mTextLives1.destroy()
        self.mTextLives1 = None
        if self.mNumPlayers == 2:
            self.mTextScore2.destroy()
            self.mTextScore2 = None
            self.mTextLives2.destroy()
            self.mTextLives2 = None

        if self.mText != None:
            self.mText.destroy()
            self.mText = None

        CGameData.inst().destroy()

    # Establece el estado actual e inicializa
    # las variables correspondientes al estado
    def setState(self, aState):
        CGameState.setState(self, aState)

        if self.getState() == CLevelState.INIT_LEVEL:
            CEnemyManager.inst().setCanShoot(False)
            self.mText = CTextSprite("NIVEL " + str(self.mLevel), 60, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
            self.mText.setXY((CGame.SCREEN_WIDTH - self.mText.getWidth()) / 2, (CGame.SCREEN_HEIGHT - self.mText.getHeight()) / 2)
            self.mText.setVisible(True)
        elif self.getState() == CLevelState.TRANSITION: 
            self.mText.setVisible(False)
        elif self.getState() == CLevelState.PLAYING:
            CEnemyManager.inst().setCanShoot(True)
            self.mText.setVisible(False)
        elif self.getState() == CLevelState.GAME_OVER:
            self.mText = CTextSprite("GAME OVER", 80, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
            self.mText.setXY((CGame.SCREEN_WIDTH - self.mText.getWidth()) / 2, (CGame.SCREEN_HEIGHT - self.mText.getHeight()) / 2)
            self.mText.setVisible(True)
            
    # Crear la formación inicial
    def initEnemies(self):
        f = 0
        while f <= 4:
            c = 0
            while c <= 4:
                n = CNave(f)
                n.setXY(100 + (70 * c), 30 + (35 * f))
                n.setVelX(4)
                n.setVelY(0)
                n.setBounds(0, 0, CGame.SCREEN_WIDTH - n.getWidth(), CGame.SCREEN_HEIGHT - n.getHeight())
                n.setBoundAction(CGameObject.NONE) 
                n.setCanShoot(False)
                CEnemyManager.inst().add(n)
                c = c + 1
            f = f + 1

        # Establecer la velocidad mínima y máxima de la formación.
        CEnemyManager.inst().setMinMaxVelX(1, 8) 

    # Función para pasar de nivel
    def nextLevel(self):
        self.mLevel = self.mLevel + 1
        self.initEnemies()
        self.setState(CLevelState.INIT_LEVEL)



        
                               