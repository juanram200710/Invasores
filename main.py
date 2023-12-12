# -*- coding: utf-8 -*-

#------------------------------------------------------------------------
# Máquina de estados del juego. Clases CGame, CGameState y CLevelState.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#------------------------------------------------------------------------

from api.CGame import *
from game.states.CMenuState import *

# ============== Punto de entrada del programa =================

# Inicializar los elementos necesarios del juego.
g = CGame()

# Crear el estado para el nivel del juego.
initState = CMenuState()
g.setState(initState)

# Loop principal del juego.
g.gameLoop()

# Liberar los recursos al final
g.destroy()
