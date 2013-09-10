'''
Created on 10.09.2013

@author: RV Administrator
'''

import Vector
GRAVITATION = 6.67384e-11

class Particle(object):
    '''
    Stellt einen Paktikel dar.
    '''


    def __init__(self, mass, x, y):
        '''
        Initialisiert die Attribute.
        '''
        self.mass = mass
        self.pos = Vector.Vector(x, y)
        self.movement = Vector.Vector()
        
    def calcMovement(self, particleField, dt):
        '''
        Berechnet den neuen Bewegungsvektor des Partikels. dt = delta Zeit
        '''
        force = Vector.Vector()
        for particle in particleField:
            r2 = Vector.DistanceSqrd(self.pos, particle.pos)        #Das Quadrat des Abstands der Partikel
            if r2:
                force += Vector.Normalize(self.pos - particle.pos) * (GRAVITATION * (self.mass * particle.mass) / r2) #Berechnet die Gesamtkraft
        a = force / self.mass       #f = m * a --> a = f / m     Beschleunigung
        v = a * dt                  #a = v / t --> v = a * t     Geschwindigkeit
        self.movement += v
    
    def move(self):
        '''
        Bewegt den Partikel
        '''
        self.pos += self.movement
        print self.pos
        
        
        
        