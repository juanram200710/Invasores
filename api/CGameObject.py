# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Clase CGameObject.
# Clase base de todos los objetos que se mueven en el juego.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

class CGameObject(object):

    # Comportamientos del objeto al llegar a un borde.
    NONE = 0    # No tiene ninguno, el objeto sigue de largo.
    STOP = 1    # El objeto se detiene al alcanzar un borde.
    WRAP = 2    # El objeto aparece por el lado contrario.
    BOUNCE = 3  # El objeto rebota en el borde.
    DIE = 4     # El objeto se marca para ser eliminado.

    def __init__(self):

        # Coordenadas del objeto.
        self.mX = 0
        self.mY = 0

        # Velocidad.
        self.mVelX = 0
        self.mVelY = 0

        # Aceleración.
        self.mAccelX = 0
        self.mAccelY = 0

        # Variables para controlar los bordes.
        self.mMinX = -float("inf")
        self.mMaxX = float("inf")
        self.mMinY = -float("inf")
        self.mMaxY = float("inf")

        # Comportamiento de borde del objeto. Ponemos que no tenga ninguno
        # por defecto, y el objeto seguirá de largo en los bordes.
        self.mBoundAction = CGameObject.NONE

        # Indica si el objeto está vivo o muerto (debe morir).
        self.mIsDead = False

        # Estado actual.
        self.mState = 0

        # Control del tiempo en el estado actual.
        self.mTimeState = 0

    # Obtener la coordenada X.
    def getX(self):
        return self.mX

    # Obtener la coordenada Y.
    def getY(self):
        return self.mY
    
    # Establecer la coordenada X del objeto.
    def setX(self, aX):
        self.mX = aX

    # Establecer la coordenada Y del objeto.
    def setY(self, aY):
        self.mY = aY    

    # Establece la posición del objeto.
    # Parámetros:
    # aX, aY: Coordenadas x e y del objeto.
    def setXY(self, aX, aY):

        self.mX = aX
        self.mY = aY

    # Establece la velocidad X del objeto.
    def setVelX(self, aVelX):

        self.mVelX = aVelX

    # Establece la velocidad Y del objeto.
    def setVelY(self, aVelY):

        self.mVelY = aVelY

    # Obtener la velocidad X.
    def getVelX(self):
        return self.mVelX

    # Obtener la velocidad Y.
    def getVelY(self):
        return self.mVelY    

    # Establece la aceleración x del objeto.
    def setAccelX(self, aAccelX):

        self.mAccelX = aAccelX

    # Establece la aceleración y del objeto.
    def setAccelY(self, aAccelY):

        self.mAccelY = aAccelY

    # Define los límites del movimiento del objeto.
    # Parámetros:
    # aMinX, aMinY: Coordenadas x e y mínimas del mundo.
    # aMaxX, aMaxY: Coordenadas x e y máximas del mundo.
    def setBounds(self, aMinX, aMinY, aMaxX, aMaxY):

        self.mMinX = aMinX
        self.mMaxX = aMaxX
        self.mMinY = aMinY
        self.mMaxY = aMaxY

    # Define el comportamiento al alcanzar los bordes del mundo.
    def setBoundAction(self, aBoundAction):
        self.mBoundAction = aBoundAction

    # Update mueve el objecto según su velocidad.
    def update(self):

        # Incrementar el tiempo del estado actual.
        self.mTimeState = self.mTimeState + 1

        # Modificar la velocidad según la aceleración.
        self.mVelX += self.mAccelX
        self.mVelY += self.mAccelY

        # Mover el objeto.
        self.mX += self.mVelX
        self.mY += self.mVelY

        # Comportamiento con el borde.
        self.checkBounds()

    # Realiza el chequeo con los bordes y aplica el comportamiento que
    # corresponda si el objeto toca alguno de los bordes.
    # Esta función es invocada en update().
    # La variable self.boundAction contiene el comportamiento:
    # NONE: No tiene ninguno, el objeto sigue de largo.
    # STOP: El objeto se detiene al alcanzar un borde.
    # WRAP: El objeto aparece por el lado contrario.
    # BOUNCE: El objeto rebota en el borde.
    # DIE: El objeto se marca para ser eliminado.
    def checkBounds(self):

        # Si el comportamiento es NONE no se chequea el borde.
        if self.mBoundAction == CGameObject.NONE:
            return

        # Saber qué bordes está tocando el objeto.
        left = (self.mX < self.mMinX)
        right = (self.mX > self.mMaxX)
        up = (self.mY < self.mMinY)
        down = (self.mY > self.mMaxY)

        # Si no toca ningún borde no hacemos nada.
        if not (left or right or up or down):
            return

        # Al llegar a este punto, el objeto está tocando un borde.
        # Hay que corregir la posición del objeto y luego modificar
        # su velocidad según el comportamiento que tenga.

        # Corregir la posición del objeto.
        # Si es WRAP, el objeto aparece desde el lado contrario.
        if (self.mBoundAction == CGameObject.WRAP):
            if (left):
                self.mX = self.mMaxX
            if (right):
                self.mX = self.mMinX
            if (up):
                self.mY = self.mMaxY
            if (down):
                self.mY = self.mMinY
        # Si es STOP, BOUNCE o DIE corregimos la posición porque sino el
        # objeto queda con parte fuera de los límites.
        else:
            if (left):
                self.mX = self.mMinX
            if (right):
                self.mX = self.mMaxX
            if (up):
                self.mY = self.mMinY
            if (down):
                self.mY = self.mMaxY

        # Si el comportamiento es STOP o DIE, el objeto se detiene.
        if (self.mBoundAction == CGameObject.STOP or self.mBoundAction == CGameObject.DIE):
            self.mVelX = 0
            self.mVelY = 0
            self.mAccelX = 0
            self.mAccelY = 0
        elif (self.mBoundAction == CGameObject.BOUNCE):
            if (right or left):
                self.mVelX *= -1
            if (up or down):
                self.mVelY *= -1

        # Si el comportamiento es que muera, se marca para morir.
        # El manager luego lo elimina.
        if (self.mBoundAction == CGameObject.DIE):
            self.mIsDead = True
            return

    # Indica si hay que eliminar el objeto o no.
    def isDead(self):
        return self.mIsDead

    # Marcar al objeto para morir. El manager lo elimina.
    def die(self):
        self.mIsDead = True

    # Detiene el movimiento del objeto.
    def stopMove(self):
        self.setVelX(0)
        self.setVelY(0)
        self.setAccelX(0)
        self.setAccelY(0)

    # Liberar lo que haya creado el objeto.
    def destroy(self):
        
        pass

    # Retorna el estado actual.
    def getState(self):
        return self.mState

    # Establece el estado actual.
    def setState(self, aState):
        self.mState = aState
        # Resetear el tiempo del estado actual.
        self.mTimeState = 0

    # Retorna el tiempo en el estado actual.
    def getTimeState(self):
        return self.mTimeState


