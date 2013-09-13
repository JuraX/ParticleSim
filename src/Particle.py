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


    def __init__(self, mass, x, y, gui):
        '''
        Initialisiert die Attribute.
        '''
        self.mass = mass
        self.pos = Vector.Vector(x, y)
        self.movement = Vector.Vector(-self.pos[1], self.pos[0]) * 0.0005
        self.collisionRadius = (math.sqrt(COLLISION_RADIUS_FACTOR * self.mass))
        self.canvas = None
        self.gui = gui
        
    def calcMovement(self, particleField, dt):
        '''
        Berechnet den neuen Bewegungsvektor des Partikels. dt = delta Zeit
        '''
        force = Vector.Vector()
        s = len(particleField)
        i = 0
        while i < len(particleField):
            particle = particleField[i]
            if particle != self:
                r2 = Vector.DistanceSqrd(self.pos, particle.pos)        #Das Quadrat des Abstands der Partikel
                if math.sqrt(r2) <= self.collisionRadius:
                    masse1 = self.mass
                    masse2 = particle.mass
                    self.mass += particle.mass
                    self.collisionRadius = (math.sqrt(COLLISION_RADIUS_FACTOR * self.mass))    #a = r**2 * pi  a/pi = r**2 r = sqrt(a/pi)
                    self.movement = (self.movement * masse1 + particle.movement * masse2) / self.mass
                    #print "PARTIKEL KOMBINIERT"
                    self.gui.delete(particle.canvas)
                    particleField.remove(particle)
                    del particle
                elif r2:
                    force -= Vector.Normalize(self.pos - particle.pos) * (GRAVITATION * (self.mass * particle.mass) / r2) #Berechnet die Gesamtkraft
            i += 1
               
        a = force / self.mass       #f = m * a --> a = f / m     Beschleunigung
        v = a * dt * FACTOR                  #a = v / t --> v = a * t     Geschwindigkeit
        self.movement += v
    
    def move(self):
        '''
        Bewegt den Partikel
        '''
        self.pos += self.movement
        
        
        
        