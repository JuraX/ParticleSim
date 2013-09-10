'''
Created on 10.09.2013

@author: RV Administrator
'''

import Vector
import math

GRAVITATION = 6.67384e-11
COLLISION_RADIUS_FACTOR = 15
FACTOR = 10000000000000

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
        self.collisionRadius = (math.sqrt(COLLISION_RADIUS_FACTOR * self.mass))
        
    def calcMovement(self, particleField, dt):
        '''
        Berechnet den neuen Bewegungsvektor des Partikels. dt = delta Zeit
        '''
        force = Vector.Vector()
        s = len(particleField)
        for i in range(0, s-1):
            particle = particleField[i]
            if particle != self:
                r2 = Vector.DistanceSqrd(self.pos, particle.pos)        #Das Quadrat des Abstands der Partikel
                if math.sqrt(r2) <= self.collisionRadius:
                    masse1 = self.mass
                    masse2 = particle.mass
                    self.mass += particle.mass
                    self.collisionRadius = (math.sqrt(COLLISION_RADIUS_FACTOR * self.mass))    #a = r**2 * pi  a/pi = r**2 r = sqrt(a/pi)
                    self.movement = (self.movement * masse1 + particle.movement * masse2) / self.mass
                    print "PARTIKEL KOMBINIERT"
                    particleField.remove(particle)
                    
                    s-=1 # Die Indizes wieder hinbiegen
                    i-=1
                if r2:
                    force -= Vector.Normalize(self.pos - particle.pos) * (GRAVITATION * (self.mass * particle.mass) / r2) #Berechnet die Gesamtkraft
               
        a = force / self.mass       #f = m * a --> a = f / m     Beschleunigung
        v = a * dt * FACTOR                  #a = v / t --> v = a * t     Geschwindigkeit
        self.movement += v
    
    def move(self):
        '''
        Bewegt den Partikel
        '''
        self.pos += self.movement
        
        
        
        