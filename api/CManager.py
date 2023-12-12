# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase Manager.
# Clase para manejar una lista con un tipo de objeto.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Importar Pygame.
import pygame

class CManager(object):

    def __init__(self):

        # Lista de objetos.
        self.mArray = []

    # Procesar los objetos.
    def update(self):
        for e in self.mArray:
            e.update()

        i = len(self.mArray)
        while i > 0:
            if self.mArray[i-1].isDead():
                self.mArray[i-1].destroy()
                self.mArray.pop(i-1)
            i = i - 1

    # Dibujar los objetos.
    def render(self, aScreen):
        for e in self.mArray:
            e.render(aScreen)

    # Agregar un objeto a la lista.
    def add(self, aElement):
        self.mArray.append(aElement)

    # Destruir todos los objetos y removerlos de la lista.
    # Destruir la lista.
    def destroy(self):
        i = len(self.mArray)
        while i > 0:
            self.mArray[i-1].destroy()
            self.mArray.pop(i-1)
            i = i - 1

        self.mArray = None

    # Determina si el sprite que se recibe como parámetro choca
    # con alguno de los sprites de la lista.
    # Retorna True si colisiona con alguno y False si no colisiona
    # con ninguno.
    def collides(self, aSprite):
        i = 0
        while i < len(self.mArray):
            if aSprite.collides(self.mArray[i]):
                return self.mArray[i]
            i = i + 1
        return None
    
    def getLength(self):
        return len(self.mArray)
    
    