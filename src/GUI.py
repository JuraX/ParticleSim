'''
Created on 10.09.2013

@author: RV Administrator
'''

from Tkinter import *
from threading import *
import Particle
import math
import Queue
import ParticleManager

SIZE = 1000



class GUI():
    def __init__(self):
        self.master = Tk()
        
        self.c = Canvas(self.master, width = SIZE, height = SIZE)
        self.c.pack()
        
        self.request_queue = Queue.Queue(maxsize = -1)
        self.result_queue = Queue.Queue(maxsize = -1)
        
        self.run()
    
    
    def run(self):
        self.pm = ParticleManager.ParticleManager(self)
        mainloop()
        
    def addParticle(self, particle):
        radius = math.sqrt(Particle.COLLISION_RADIUS_FACTOR * particle.mass)*self.pm.faktor
        if radius < 1:
            radius = 1
        self.c.delete(particle.canvas)
        particle.canvas = self.c.create_oval((SIZE/2.0/self.pm.faktor + particle.pos[0])*self.pm.faktor - radius, (SIZE/2.0/self.pm.faktor + particle.pos[1])*self.pm.faktor - radius, (SIZE/2.0/self.pm.faktor + particle.pos[0])*self.pm.faktor + radius, (SIZE/2.0/self.pm.faktor + particle.pos[1])*self.pm.faktor + radius, fill = "black")
   
    

        
        
if __name__ == '__main__':   
    g = GUI()
    
    
    
    
    
    
    
    
    
    
    
    
    