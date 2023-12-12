# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CGame.
# Clase que maneja todos los estados del juego a nivel de aplicación.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Import pygame
import pygame

# Clase CKeyboard
from api.CKeyboard import *

# Clase CMouse
from api.CMouse import *

# Clase CMousePointer
from game.CMousePointer import *

# Importar el garbage collector
import gc

# Clase CGameConstants
from api.CGameConstants import *

from api.CTextSprite import *

class CGame(object):

    mInstance = None
    mInitialized = False

    mScreen = None
    mClock = None
    mSalir = False
    mMousePointer = None

    # Variable para mostrar o no el puntero del mouse
    mShowGamePointer = False

    # Pantalla (estado) actual del juego
    mState = None
 
    SCREEN_WIDTH = 0
    SCREEN_HEIGHT = 0
    RESOLUTION = 0

    # Control del modo ventana o fullscreen
    mIsFullScreen = False

    # Pausa.
    mIsPaused = False
    mTextPause = None

    # FPS del juego
    FPS = 60

    def __new__(self, *args, **kargs):
        if (CGame.mInstance is None):
            CGame.mInstance = object.__new__(self, *args, **kargs)
            self.init(CGame.mInstance)
        else:
            print("Cuidado: Game(): no se debería instanciar más de una vez esta clase. Usar Game.inst().")
        return self.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance

    # Función de inicialización
    def init(self):
        if (CGame.mInitialized):
            return
        CGame.mInitialized = True

        # Definir ancho y alto de la pantalla
        CGame.SCREEN_WIDTH = CGameConstants.SCREEN_WIDTH
        CGame.SCREEN_HEIGHT = CGameConstants.SCREEN_HEIGHT
        CGame.RESOLUTION = (CGame.SCREEN_WIDTH, CGame.SCREEN_HEIGHT)   

        # Inicializar Pygame
        pygame.init()

        # Inicializar el mixer de audio de Pygame
        pygame.mixer.init()

        # Poner el modo de video en ventana e indicar la resolución
        CGame.mScreen = pygame.display.set_mode(CGame.RESOLUTION) 
        # Poner el título de la ventana
        pygame.display.set_caption("Invasores Espaciales")

        # Crear la superficie del fondo o background
        CGame.mBackground = pygame.Surface(self.mScreen.get_size())
        CGame.mBackground = self.mBackground.convert()

        # Inicializar el reloj
        CGame.mClock = pygame.time.Clock()

        # Inicializar la variable de control del game loop
        CGame.mSalir = False
 
        self.mShowGamePointer = False
        self.showGamePointer(False)

        CGame.mState = None

        # Variables para la pausa.
        CGame.mIsPaused = False
        CGame.mTextPause = CTextSprite("JUEGO EN PAUSA", 40, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
        CGame.mTextPause.setXY((CGame.SCREEN_WIDTH - CGame.mTextPause.getWidth()) / 2, (CGame.SCREEN_HEIGHT - CGame.mTextPause.getHeight()) / 2)

    # Función para cambiar entre pantallas (estados) del juego
    def setState(self, aState):
        if (CGame.mState != None):
            CGame.mState.destroy()
            CGame.mState = None
            # Liberar memoria
            print(gc.collect(), "Objetos borrados")

        CGame.mState = aState
        CGame.mState.init()

    # Game loop del juego
    def gameLoop(self):

        while not self.mSalir:
            self.update()
            self.render()

    # Correr la lógica del juego
    def update(self):

        # Timer que controla el frame rate
        CGame.mClock.tick(CGame.FPS)

        # Llamar a update de CKeyboard
        CKeyboard.inst().update()

        # Llamar a update de CMouse
        CMouse.inst().update()

        # Actualizar el sprite del puntero del mouse
        if (CGame.mMousePointer != None):
            CGame.mMousePointer.update()

        # Procesar los eventos que llegan a la aplicación 
        for event in pygame.event.get():

            # Si se cierra la ventana se sale del programa
            if event.type == pygame.QUIT:
                CGame.mSalir = True

            # Si se pulsa la tecla [Esc] se sale del programa
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_ESCAPE):
                    CGame.mSalir = True    

            # Si se pulsa la tecla(F), se cambia entre la ventana y fullscreen.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    CGame.mIsFullScreen = not self.mIsFullScreen
                    if self.mIsFullScreen:
                        CGame.mScreen = pygame.display.set_mode(CGame.RESOLUTION, pygame.FULLSCREEN) 
                    else:
                        CGame.mScreen = pygame.display.set_mode(CGame.RESOLUTION)

            # Registrar cuando se presiona o se suelta una tecla.
            if event.type == pygame.KEYDOWN:
                CKeyboard.inst().keyDown(event.key)
            if event.type == pygame.KEYUP:
                CKeyboard.inst().keyUp(event.key)

        if CKeyboard.inst().pauseKey():
            self.togglePause()

        # Cuando el juego está en pausa no se corre update()
        if not CGame.mIsPaused:
            # Actualizar el estado del juego
            CGame.mState.update()        

    def render(self):

        # Dibujar el fondo
        CGame.mScreen.blit(self.mBackground, (0, 0))

        # Dibujar el estado del juego
        CGame.mState.render()

        # Si el juego está en pausa se muestra el mensaje.
        if CGame.mIsPaused:
            CGame.mTextPause.render(self.mScreen)


        # Dibujar el puntero del mouse
        if (CGame.mMousePointer != None):
            CGame.mMousePointer.render(self.mScreen)

        # Actualizar la pantalla
        pygame.display.flip()

    def setBackground(self, aBackgroundImage):
        CGame.mBackground = None
        CGame.mBackground = aBackgroundImage
        self.blitBackground(CGame.mBackground)

    def blitBackground(self, aBackgroundImage):
        CGame.mScreen.blit(aBackgroundImage, (9, 0))

    # Obtener la referencia a la pantalla (usada para dibujar)
    def getScreen(self):
        return CGame.mScreen
    
    def togglePause(self):
        CGame.mIsPaused = not CGame.mIsPaused

    def destroy(self):
        if (CGame.mState != None):
            CGame.mState.destroy()
            CGame.mState = None

        CKeyboard.inst().destroy()
        CMouse.inst().destroy()

        # Destruir el puntero del mouse
        if (CGame.mMousePointer != None):
            CGame.mMousePointer.destroy()
            CGame.mMousePointer = None
        pygame.mouse.set_visible(True)
 
        CGame.mTextPause.destroy()
        CGame.mTextPause = None

        CGame.mInstance = None

        # Cerrar pygame y liberar los recursos que pidió el programa
        pygame.quit() 

    def showGamePointer(self, aShowGamePointer):
        self.mShowGamePointer = aShowGamePointer

        if (aShowGamePointer):
            if (CGame.mMousePointer == None):
                # Crear el sprite del puntero del mouse
                CGame.mMousePointer = CMousePointer()
            # Ocultar el puntero del sistema
            pygame.mouse.set_visible(False)
        else:
            # Eliminar el sprite del puntero del mouse.
            if (CGame.mMousePointer != None):
                CGame.mMousePointer.destroy()
                CGame.mMousePointer = None
            # Mostrar el puntero del sistema
            pygame.mouse.set_visible(True)                                                                       



