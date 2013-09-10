'''
Created on 10.09.2013

@author: RV Administrator
'''

import Vector
GRAVITATION = 6.67384e11

class Particle(object):
    '''
    Stellt einen Paktikel dar.
    '''


    def __init__(self, mass, x, y):
        '''
        Initialisiert die Attribute.
        '''
        self.mass = mass
        self.pos = Vector(x, y)
        self.movement = Vector.Vector()
        
    def calcMovement(self, particleField, dt):
        '''
        Berechnet den neuen Bewegungsvektor des Partikels. dt = delta Zeit
        '''
        force = Vector.Vector()
        for particle in particleField:
            r2 = Vector.DistanceSqrd(self.pos, particle.pos)        #Das Quadrat des Abstands der Partikel
            force += GRAVITATION * (self.mass * particle.mass) / r2 * (self.pos - particle.pos) #Berechnet die Gesamtkraft
        a = force / self.mass       #f = m * a --> a = f / m     Beschleunigung
        v = a / dt
        self.movement += v