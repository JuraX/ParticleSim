'''
Created on 10.09.2013

@author: RV Administrator
'''

from Tkinter import *
from threading import *
import Particle
import math
import Queue
from ParticleManager import *

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
        self.pm = ParticleManager(self)
        mainloop()
        
    def addParticle(self, particle):
        radius = math.sqrt(Particle.COLLISION_RADIUS_FACTOR * particle.mass)
        if radius < 1:
            radius = 1
        self.c.delete(particle.canvas)
        particle.canvas = self.c.create_oval(SIZE/2.0 + particle.pos[0] - radius, SIZE/2.0 + particle.pos[1] - radius, SIZE/2.0 + particle.pos[0] + radius, SIZE/2.0 + particle.pos[1] + radius, fill = "black")
   
    

        
        
if __name__ == '__main__':   
    g = GUI()
    
    
    
    
    
    
    
    
    
    
    
    
    