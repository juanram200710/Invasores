# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CMenuState.
# Maneja el menú principal del juego.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

import pygame
from api.CKeyboard import *
from api.CGame import *
from api.CGameState import *
from api.CTextSprite import *

class CMenuState(CGameState):

    mImgSpace = None

    mTextTitle = None
    mTextPressFire = None

    def __init__(self):
        CGameState.__init__(self)

        self.mImgSpace = None
        self.mTextTitle = None
        self.mTextPressFire = None

    def init(self):
        CGameState.init(self)

        # Cargar la imagen del fondo. Que es una imagen de 640 x 360
        self.mImgSpace = pygame.image.load("assets/images/menu_640x360.jpg")
        self.mImgSpace = self.mImgSpace.convert()
        # Dibujar la imagen cargada en la imagen de fondo del juego.
        CGame.inst().setBackground(self.mImgSpace)

        self.mTextTitle = CTextSprite("INVASORES", 60, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF)) 
        self.mTextTitle.setXY((CGame.SCREEN_WIDTH - self.mTextTitle.getWidth()) / 2, 20)
        self.mTextPressFire = CTextSprite("Pulsa: [Space] = un jugador, [Q] = Dos jugadores ...", 20, "assets/fonts/days.otf", (0xFF, 0xFF, 0xFF))
        self.mTextPressFire.setXY((CGame.SCREEN_WIDTH - self.mTextPressFire.getWidth()) / 2, 330)

        # Mostrar el sprite del puntero del mouse.
        CGame.inst().showGamePointer(True)
        

    def update(self):
        CGameState.update(self)

        if CKeyboard.inst().fire():
            from game.states.CLevelState import CLevelState
            nextState = CLevelState(1)
            CGame.inst().setState(nextState)
            return
        
        if CKeyboard.inst().fire2():
            from game.states.CLevelState import CLevelState
            nextState = CLevelState(2)
            CGame.inst().setState(nextState)
            return

        self.mTextTitle.update()
        self.mTextPressFire.update()

    def render(self):
        CGameState.render(self)

        self.mTextTitle.render(CGame.inst().getScreen())
        self.mTextPressFire.render(CGame.inst().getScreen())

    def destroy(self):
        CGameState.destroy(self)

        self.mImgSpace = None

        self.mTextTitle.destroy()
        self.mTextTitle = None
        self.mTextPressFire.destroy()
        self.mTextPressFire = None

                                       
