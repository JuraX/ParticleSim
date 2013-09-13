'''
Created on 10.09.2013

@author: RV Administrator
'''

import Particle
from random import  *
import GUI
import time
from threading import *

F=2
MASS_MIN = 0.01*F
MASS_MAX = 0.1*F
COORDS = 500.
SIZE = 1000
GAUSS = 100
AMOUT = 250

class ParticleManager(Thread):
    def __init__(self, gui):
        Thread.__init__(self)
        self.gui = gui
        self.high = 500.
        self.faktor = SIZE / self.high
        self.start()
    def run(self):
        g = self.gui
        particles = []
        for i in range(AMOUT):
            particles.append(Particle.Particle(random()*(MASS_MAX - MASS_MIN) + MASS_MIN, (COORDS - gauss(COORDS, GAUSS)), (COORDS - gauss(COORDS, GAUSS)), g.c))
        while 1:
            start = time.time()
            for j in particles:
                j.calcMovement(particles, 0.01)
                if abs(j.pos[0]*2) > self.high and self.faktor > 0.7:
                    print "+",
                    self.high *= 1.25
                    self.faktor = SIZE / self.high
                    print self.faktor
                if abs(j.pos[1]*2) > self.high and self.faktor > 0.7:
                    print "+",
                    self.high *= 1.25
                    self.faktor = SIZE / self.high
                    print self.faktor
            for j in particles:
                j.move()
                g.addParticle(j)
            if time.time() - start <= 0.01:
                time.sleep(0.01 - time.time() + start)
                
                
                
                
                
                
                
                
                
                
                