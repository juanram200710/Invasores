# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------
# Clase CAudioManager
# Clase para manejar el audio y los canales.
#
# Autor: Eliott Amaya Domínguez
# Proyecto: Invasores Espaciales
# Licencia: Creative Commons. BY-NC-SA.
#--------------------------------------------------------------------------------

# Importar Pygame
import pygame

class CAudioManager(object):

    mInstance = None
    mInitialized = False

    mChannels = 8 

    def __new__(self, *args, **kargs):
        if (CAudioManager.mInstance is None):
            CAudioManager.mInstance = object.__new__(self, *args, **kargs)
            self.init(CAudioManager.mInstance)
        else:
            print("Cuidado: CAudioManager(): No se debería instanciar más de una vez esta clase. Usar CAudioManager.inst()")    
        return CAudioManager.mInstance

    @classmethod
    def inst(cls):
        if (not cls.mInstance):
            return cls()
        return cls.mInstance
    
    def init(self):
        if (CAudioManager.mInitialized):
            return
        CAudioManager.mInitialized = True

        CAudioManager.mChannels = pygame.mixer.get_num_channels()

        # Crear el sonido de disparo del jugador
        CAudioManager.mSoundShootPlayer = pygame.mixer.Sound("assets/audio/player_shoot.wav")
        # Sonido hit
        CAudioManager.mSoundHitPlayer = pygame.mixer.Sound("assets/audio/player_hit.wav")
        # Sonido de la explosión del jugador
        CAudioManager.mSoundExplosionPlayer = pygame.mixer.Sound("assets/audio/player_explosion.wav")
        # Sonido del disparo del enemigo
        CAudioManager.mSoundShootEnemy = pygame.mixer.Sound("assets/audio/enemy_shoot.wav")
        # Sonido de la explosión del enemigo
        CAudioManager.mSoundExplosionEnemy = pygame.mixer.Sound("assets/audio/enemy_explosion.wav")
        # Sonido de la muerte de las balas
        CAudioManager.mSoundCannotShoot = pygame.mixer.Sound("assets/audio/player_cannot_shoot.wav")

    def play(self, aSound):
        CAudioManager.inst().getChannel().play(aSound)

    def getChannel(self):
        c = pygame.mixer.find_channel(True)
        while c is None:
            CAudioManager.mChannels += 1
            pygame.mixer.set_num_channels(CAudioManager.mChannels)
            c = pygame.mixer.find_channel()
        return c
    
    def destroy(self):
        CAudioManager.mInstance = None

        CAudioManager.mSoundShootPlayer = None
        CAudioManager.mSoundHitPlayer = None
        CAudioManager.mSoundExplosionPlayer = None
        CAudioManager.mSoundShootEnemy = None
        CAudioManager.mSoundExplosionEnemy = None
        CAudioManager.mSoundCannotShoot = None
        






