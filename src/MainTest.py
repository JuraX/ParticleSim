'''
Created on 10.09.2013

@author: RV Administrator
'''

import Particle, random

if __name__ == '__main__':
    particles = []
    for i in range(5):
        particles.append(Particle.Particle(random.randint(1, 10), random.random() * 10 - 5, random.random() * 10 - 5))