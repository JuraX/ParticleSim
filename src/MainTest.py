'''
Created on 10.09.2013

@author: RV Administrator
'''

import Particle
from random import  *

MASS_MIN = 1
MASS_MAX = 10
COORDS_MIN = -5
COORDS_MAX = 5

if __name__ == '__main__':
    particles = []
    for i in range(5):
        particles.append(Particle.Particle(random()*(MASS_MAX - MASS_MIN) + MASS_MIN, random()*(COORDS_MAX - COORDS_MIN) + COORDS_MIN, random()*(COORDS_MAX - COORDS_MIN) + COORDS_MIN))
    for i in xrange(100):
        for j in particles:
            j.calcMovement(particles, 0.01)
        for j in particles:
            j.move()
        print '--------------------------'