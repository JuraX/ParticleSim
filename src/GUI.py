'''
Created on 10.09.2013

@author: RV Administrator
'''

from Tkinter import *
from threading import *
import Particle
import math

SIZE = 800

class GUI(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.master = Tk()
        
        self.c = Canvas(self.master, width = SIZE, height = SIZE)
        self.c.pack()
        
        self.start()
    
    
    def run(self):
        mainloop()
        
    def addParticle(self, particle):
        radius = math.sqrt(Particle.COLLISION_RADIUS_FACTOR * particle.mass)
        if radius < 1:
            radius = 1
        self.c.create_oval(SIZE/2.0 + particle.pos[0] - radius, SIZE/2.0 + particle.pos[1] - radius, SIZE/2.0 + particle.pos[0] + radius, SIZE/2.0 + particle.pos[1] + radius, fill = "black")
   
    def clearall(self):
        self.c.delete(ALL)
        
        
if __name__ == '__main__':   
    g = GUI()
    g.c.create_oval(300, 300, 300, 300, fill = "blue")