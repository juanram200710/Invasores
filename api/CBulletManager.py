# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CBulletManager.
# Clase para manejar los disparos del juego.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Importar Pygame.
import pygame

# Importar la clase base del manager.
from api.CManager import *

class CBulletManager(CManager):

    mInstance = None
    mInitialized = False

    def __new__(self, *args, **kargs):
        if (CBulletManager.mInstance is None):
            CBulletManager.mInstance = object.__new__(self, *args, **kargs)
            self.init(CBulletManager.mInstance)
        else:
            print("Cuidado: CBulletManager(): No se debería instanciar más de una vez esta clase. Usar CBulletManager.inst().")
        return self.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        if (CBulletManager.mInitialized):
            return
        CBulletManager.mInitialized = True

        # Invocar al constructor de la clase base que crea la lista.
        CManager.__init__(self)

    # Procesar los objetos.
    def update(self):
        CManager.update(self)

    # Dibujar los objetos.
    def render(self, aScreen):
        CManager.render(self, aScreen)

    # Agregar un objeto a la lista.
    def add(self, aBullet):
        CManager.add(self, aBullet)

    # Destruir todos los objetos y removerlos de la lista.
    # Destruir la lista.
    def destroy(self):
        CManager.destroy(self)

        CBulletManager.mInstance = None

