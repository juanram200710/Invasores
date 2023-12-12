# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CEnemyManager.
# Clase para manejar los enemigos del juego.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase base del manager.
from api.CManager import *
from api.CGameConstants import *
from game.CEnemyBullet import *

class CEnemyManager(CManager):

    mInstance = None
    mInitialized = False

    # Constantes para la dirección de la formación de enemigos.
    RIGHT = 0
    LEFT = 1

    # Dirección de la formación.
    mDirection = RIGHT

    # Variable para la velocidad de la formación de enemigos.
    mMinVelX = 0
    mMaxVelX = 0
    mVelX = 0
    mMaxShips = 0

    def __new__(self, *args, **kargs):
        if (CEnemyManager.mInstance is None):
            CEnemyManager.mInstance = object.__new__(self, *args, **kargs)
            self.init(CEnemyManager.mInstance)
        else:
            print("Cuidado: CEnemyManager(): No se debería instanciar más de una vez esta clase. Usar CEnemyManager.inst().")
        return self.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        if (CEnemyManager.mInitialized):
            return
        CEnemyManager.mInitialized = True

        # Invocar al constructor de la clase base que crea la lista.
        CManager.__init__(self)

    # Procesar los objetos.
    def update(self):
        CManager.update(self)

        # Establecer la velocidad de la formación según la cantidad de enemigos.
        if self.countShips() != 0:
            # Vale 1 cuando hay un solo enemigo y 0 cuando están
            # todos los enemigos. En el medio se interpola.
            percent = 1 - (float(self.countShips())) / float(self.mMaxShips)
        else: percent = 0

        vel = self.mMinVelX + ((self.mMaxVelX - self.mMinVelX) * percent)

        if CEnemyManager.mDirection == CEnemyManager.RIGHT:
            self.setVelX(vel)
        else:
            self.setVelX(-vel)    

        # Ver si alguno de los enemigos tocó el borde de la pantalla.
        # Si esto es así, bajar a los enemigos y luego invertir la
        # velocidad de todos los enemigos.

        touched = False
        i = 0
        while i < len(self.mArray):
        
            if not isinstance(self.mArray[i], CEnemyBullet):

                # Ver si van a la derecha y tocan el borde derecho.
                if CEnemyManager.mDirection == CEnemyManager.RIGHT:
                    if self.mArray[i].getX() + self.mArray[i].getWidth() > CGameConstants.SCREEN_WIDTH:
                        touched = True
                        break
                    # Ver so van a la izquierda y tocan el borde izquierdo.
                else:
                    if self.mArray[i].getX() < 0:
                        touched = True
                        break

            i = i + 1
        if touched:
            self.invertFormation()

    # Dibujar los objetos.
    def render(self, aScreen):
        CManager.render(self, aScreen)

    # Agregar un objeto a la lista.
    def add(self, aEnemy):
        CManager.add(self, aEnemy)

    # Destruir todos los objetos y removerlos de la lista.
    # Destruir la lista.
    def destroy(self):
        CManager.destroy(self)

        CEnemyManager.mInstance = None

    # Bajar los enemigos e invertir las velocidades de los enemigos.
    def invertFormation(self):
        if CEnemyManager.mDirection == CEnemyManager.RIGHT:
            CEnemyManager.mDirection = CEnemyManager.LEFT
        else:
            CEnemyManager.mDirection = CEnemyManager.RIGHT

        i = 0
        while i < len(self.mArray):
            if not isinstance(self.mArray[i], CEnemyBullet):
                self.mArray[i].setY(self.mArray[i].getY() + self.mArray[i].getHeight() / 2)
                self.mArray[i].setVelX(self.mArray[i].getVelX() * -1)

            i = i + 1
    
    # Establecer la velocidad mínima y máxima de la formación.
    def setMinMaxVelX(self, aMinVelX, aMaxVelX):
        self.mMinVelX = aMinVelX
        self.mMaxVelX = aMaxVelX
        self.setVelX(aMinVelX)
        self.mMaxShips = self.countShips()

    # Establecer la velocidad actual de la formación
    def setVelX(self, aMinVelX):
        self.mVelX = aMinVelX

        i = 0
        while i < len(self.mArray):
            if not isinstance(self.mArray[i], CEnemyBullet):
                self.mArray[i].setVelX(self.mVelX)
            i = i + 1

    # Retorna la cantidad de naves en la formación
    def countShips(self):
        c = 0
        i = 0

        while i < len(self.mArray):
            if not isinstance(self.mArray[i], CEnemyBullet):
                c = c + 1
            i = i + 1
        return c
    
    # Establecer si los enemigos pueden dispara o no.
    def setCanShoot(self, aCanShoot):
        i = 0
        while i < len(self.mArray):

            if not isinstance(self.mArray[i], CEnemyBullet):
                self.mArray[i].setCanShoot(aCanShoot)

            i = i + 1
                
                    


                
                                               

