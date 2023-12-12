# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CGameState.
# Es la clase base de todos los estados del juego.
# Los estados del juego heredan de esta clase porque se les invoca
# los métodos init, update, render y destroy desde la clase CGame
# que es la que maneja los estados.

# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

class CGameState(object):

    def __init__(self):

        # Estado actual
        self.mState = 0

        # Control del tiempo en el estado actual.
        self.mTimeState = 0

    def init(self):
        pass

    def update(self):
        # Incrementar el tiempo del estado actual
        self.mTimeState = self.mTimeState + 1

    def render(self):
        pass

    def destroy(self):
        pass

    # Retornar el estado actual
    def getState(self):
        return self.mState
    
    # Establecer el estado actual
    def setState(self, aState):
        self.mState = aState
        # Resetear el tiempo del estado actual
        self.mTimeState = 0

    # Retornar el tiempo en el estado actual.
    def getTimeState(self):
        return self.mTimeState  
                        