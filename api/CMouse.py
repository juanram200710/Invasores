# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CMouse.
# Clase para manejar el estado de los botones del mouse y la posición.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

# Importar Pygame
import pygame

class CMouse(object):

    mInstance = None
    mInitialized = False

    mLeftPressed = False
    mRightPressed = False
    mCenterPressed = False
 
    mLeftPressedPreviousFrame = False

    def __new__(self, *args, **kargs):
        if (CMouse.mInstance is None):
            CMouse.mInstance = object.__new__(self, *args, **kargs)
            self.init(CMouse.mInstance)
        else:
            print("Cuidado: Mouse(): No se debería instanciar más de una vez esta clase. Usar Mouse.inst().")
        return CMouse.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        if (CMouse.mInitialized):
            return
        CMouse.mInitialized = True

        CMouse.mLeftPressed = False
        CMouse.mRightPressed = False
        CMouse.mCenterPressed = False
        CMouse.mLeftPressedPreviousFrame = False

    def update(self):
        CMouse.mLeftPressedPreviousFrame = CMouse.mLeftPressed
        CMouse.mLeftPressed = pygame.mouse.get_pressed()[0]
        CMouse.mRightPressed = pygame.mouse.get_pressed()[2]
        CMouse.mCenterPressed = pygame.mouse.get_pressed()[1]

    def leftPressed(self):        
        return CMouse.mLeftPressed
    
    def rightPressed(self):
        return CMouse.mRightPressed
    
    def centerPressed(self):
        return CMouse.mCenterPressed
    
    def click(self):
        return CMouse.mLeftPressed == False and CMouse.mLeftPressedPreviousFrame == True
    
    def getPos(self):
        return pygame.mouse.get_pos()
    
    def getX(self):
        return pygame.mouse.get_pos()[0]
    
    def getY(self):
        return pygame.mouse.get_pos()[1]
    
    def destroy(self):
        CMouse.mInstance = None
        