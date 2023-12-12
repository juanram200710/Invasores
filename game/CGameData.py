# *- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CGameData
# Clase para manejar los datos del juego
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

# Importar pygame
import pygame

class CGameData(object):

    mInstance = None
    mInitialized = False

    mScore1 = 0
    mLives1 = 0
    mScore2 = 0
    mLives2 = 0

    def __new__(self, *args, **kargs):
        if (CGameData.mInstance is None):
            CGameData.mInstance = object.__new__(self, *args, **kargs)
            self.init(CGameData.mInstance)
        else:
            print("Cuidado: CGameData(): No se debería instanciar más de una vez esta clase. Usar CGameData.inst().")    
        return CGameData.mInstance
    
    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        if (CGameData.mInitialized):
            return
        CGameData.mInitialized = True

        CGameData.mScore1 = 0
        CGameData.mLives1 = 0
        CGameData.mScore2 = 0
        CGameData.mLives2 = 0

    def setScore1(self, aScore):
        CGameData.mScore1 = aScore
        self.controlScores()

    def setScore2(self, aScore):
        CGameData.mScore2 = aScore
        self.controlScores()

    def addScore1(self, aScore):
        CGameData.mScore1 += aScore
        self.controlScores()

    def addScore2(self, aScore):
        CGameData.mScore2 += aScore
        self.controlScores() 

    def controlScores(self):
        # Controlar que los scores no sean negativos o muy grandes
        if (CGameData.mScore1 < 0):
            CGameData.mScore1 = 0
        if (CGameData.mScore1 > 999999):
            CGameData.mScore1 = 999999
        if (CGameData.mScore2 < 0):
            CGameData.mScore2 = 0
        if (CGameData.mScore2 > 999999):
            CGameData.mScore2 = 999999 

    def getScore1(self):
        return CGameData.mScore1

    def getScore2(self):
        return CGameData.mScore2

    def setLives1(self, aLives):
        CGameData.mLives1 = aLives
        self.controlLives()

    def setLives2(self, aLives):
        CGameData.mLives2 = aLives
        self.controlLives()

    def addLives1(self, aLives):
        CGameData.mLives1 += aLives
        self.controlLives()

    def addLives2(self, aLives):
        CGameData.mLives2 += aLives
        self.controlLives()

    def controlLives(self): 
        # Controlar que las vidas no sean negativas o muy grandes.
        if (CGameData.mLives1 < 0):
            CGameData.mLives1 = 0
        if (CGameData.mLives1 > 9):
            CGameData.mLives1 = 9
        if (CGameData.mLives2 < 0):
            CGameData.mLives2 = 0
        if (CGameData.mLives2 > 9):
            CGameData.mLives2 = 9

    def getLives1(self):
        return CGameData.mLives1
    
    def getLives2(self):
        return CGameData.mLives2
    
    def destroy(self):
        CGameData.mInstance = None
                                                     


            
                                   


