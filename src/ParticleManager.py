'''
Created on 10.09.2013

@author: RV Administrator
'''

import Particle
from random import  *
import GUI
import time
from threading import *

MASS_MIN = 1
MASS_MAX = 10
COORDS_MIN = -300.
COORDS_MAX = 300.

class ParticleManager(Thread):
    def __init__(self, gui):
        Thread.__init__(self)
        self.gui = gui
        self.start()
    def run(self):
        g = self.gui
        particles = []
        for i in range(20):
            particles.append(Particle.Particle(random()*(MASS_MAX - MASS_MIN) + MASS_MIN, random()*(COORDS_MAX - COORDS_MIN) + COORDS_MIN, random()*(COORDS_MAX - COORDS_MIN) + COORDS_MIN))
        while 1:
            for j in particles:
                j.calcMovement(particles, 0.01)
            g.clearall()
            for j in particles:
                j.move()
                g.addParticle(j)
            time.sleep(0.02)