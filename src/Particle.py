'''
Created on 10.09.2013

@author: RV Administrator
'''

import Vector
GRAVITATION = 6.67384e-11
COLLISION_RADIUS_FACTOR = 0.2

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
        self.collisionRadius = (COLLISION_RADIUS_FACTOR * mass)
        
    def calcMovement(self, particleField, dt):
        '''
        Berechnet den neuen Bewegungsvektor des Partikels. dt = delta Zeit
        '''
        force = Vector.Vector()
        s = len(particleField)
        for i in range(0, s-1):
            particle = particleField[i]
            r2 = Vector.DistanceSqrd(self.pos, particle.pos)        #Das Quadrat des Abstands der Partikel
            if r2 <= self.collisionRadius:
                self.mass += particle.mass
                self.collisionRadius = (COLLISION_RADIUS_FACTOR * self.mass)
                particleField.remove(particle)
                
                s-=1 # Die Indizes wieder hinbiegen
                i-=1
            
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
        
        
        
        