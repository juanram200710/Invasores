# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CKeyboard.
# Clase para manejar el estado de las teclas en el juego.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

# Importar Pygame.
import pygame

class CKeyboard(object):

    mInstance = None
    mInitialized = False

    mLeftPressed = False
    mRightPressed = False
    mUpPressed = False
    mDownPressed = False
    mAPressed = False
    mDPressed = False
    mWPressed = False
    mSPressed = False

    # Estado de la tecla [Space] en el frame anterior.
    mSpacePressedPreviousFrame = False
    mSpacePressed = False
    # Estado de la tecla [Q] en el frame anterior.
    mQPressedPreviousFrame = False
    mQPressed = False

    mPPressed = False
    mPPressedPreviousFrame = False
    mEnterPressed = False
    mEnterPressedPreviousFrame = False

    def __new__(self, *args, **kargs):
        if (CKeyboard.mInstance is None):
            CKeyboard.mInstance = object.__new__(self, *args, **kargs)
            self.init(CKeyboard.mInstance)
        else:
            print("Cuidado: CKeyboard(): No se debería instanciar más de una vez esta clase. Usar CKeyboard.inst().")
        return CKeyboard.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        if (CKeyboard.mInitialized):
            return
        CKeyboard.mInitialized = True

        CKeyboard.mLeftPressed = False
        CKeyboard.mRightPressed = False
        CKeyboard.mUpPressed = False
        CKeyboard.mDownPressed = False
        CKeyboard.mAPressed = False
        CKeyboard.mDPressed = False
        CKeyboard.mWPressed = False
        CKeyboard.mSPressed = False

        CKeyboard.mSpacePressedPreviousFrame = False
        CKeyboard.mSpacePressed = False
        CKeyboard.mQPressedPreviousFrame = False
        CKeyboard.mQPressed = False

        CKeyboard.mPPressed = False
        CKeyboard.mEnterPressed = False
        CKeyboard.mPPressedPreviousFrame = False
        CKeyboard.mEnterPressedPreviousFrame = False
        
    def keyDown(self, key):
        if (key == pygame.K_LEFT):
            CKeyboard.mLeftPressed = True
        if (key == pygame.K_RIGHT):
            CKeyboard.mRightPressed = True
        if (key == pygame.K_UP):
            CKeyboard.mUpPressed = True
        if (key == pygame.K_DOWN):
            CKeyboard.mDownPressed = True
        if (key == pygame.K_SPACE):
            CKeyboard.mSpacePressed = True
        if (key == pygame.K_a):
            CKeyboard.mAPressed = True
        if (key == pygame.K_d):
            CKeyboard.mDPressed = True
        if (key == pygame.K_w):
            CKeyboard.mWPressed = True
        if (key == pygame.K_s):
            CKeyboard.mSPressed = True
        if (key == pygame.K_q):
            CKeyboard.mQPressed = True
        if (key == pygame.K_p):
            CKeyboard.mPPressed = True
        if (key == pygame.K_RETURN):
            CKeyboard.mEnterPressed = True        

    def keyUp(self, key):
        if (key == pygame.K_LEFT):
            CKeyboard.mLeftPressed = False
        if (key == pygame.K_RIGHT):
            CKeyboard.mRightPressed = False
        if (key == pygame.K_UP):
            CKeyboard.mUpPressed = False
        if (key == pygame.K_DOWN):
            CKeyboard.mDownPressed = False
        if (key == pygame.K_SPACE):
            CKeyboard.mSpacePressed = False
        if (key == pygame.K_a):
            CKeyboard.mAPressed = False
        if (key == pygame.K_d):
            CKeyboard.mDPressed = False
        if (key == pygame.K_w):
            CKeyboard.mWPressed = False
        if (key == pygame.K_s):
            CKeyboard.mSPressed = False
        if (key == pygame.K_q):
            CKeyboard.mQPressed = False
        if (key == pygame.K_p):
            CKeyboard.mPPressed = False
        if (key == pygame.K_RETURN):
            CKeyboard.mEnterPressed = False        

    # Actualiza el estado de la tecla [Space].
    def update(self):
        CKeyboard.mSpacePressedPreviousFrame = CKeyboard.mSpacePressed
        CKeyboard.mQPressedPreviousFrame = CKeyboard.mQPressed
        CKeyboard.mPPressedPreviousFrame = CKeyboard.mPPressed
        CKeyboard.mEnterPressedPreviousFrame = CKeyboard.mEnterPressed

    def leftPressed(self):
        return CKeyboard.mLeftPressed

    def rightPressed(self):
        return CKeyboard.mRightPressed

    def upPressed(self):
        return CKeyboard.mUpPressed

    def downPressed(self):
        return CKeyboard.mDownPressed

    def spacePressed(self):
        return CKeyboard.mSpacePressed

    def APressed(self):
        return CKeyboard.mAPressed

    def DPressed(self):
        return CKeyboard.mDPressed

    def WPressed(self):
        return CKeyboard.mWPressed

    def SPressed(self):
        return CKeyboard.mSPressed

    def QPressed(self):
        return CKeyboard.mQPressed

    # Función usada para disparar.
    # Solo retorna True en el momento en que se apreta la tecla.
    def fire(self):
        return CKeyboard.mSpacePressed == True and CKeyboard.mSpacePressedPreviousFrame == False

    # Función usada para disparar.
    # Solo retorna True en el momento en que se apreta la tecla.
    def fire2(self):
        return CKeyboard.mQPressed == True and CKeyboard.mQPressedPreviousFrame == False

    def pauseKey(self):
        return (CKeyboard.mPPressed == True and CKeyboard.mPPressedPreviousFrame == False) or (CKeyboard.mEnterPressed == True and CKeyboard.mEnterPressedPreviousFrame == False)
    
    def destroy(self):
        CKeyboard.mInstance = None
