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
        
        #self.c.bind("<1>", self.startmove)
        #self.c.bind("<B1-Motion>", self.move)
        #self.c.bind("<ButtonRelease-1>", self.endmove)
        #self.c.bind('<MouseWheel>', self.zoom)
        #self.c.bind("<Button-4>", self.zoom)
        #self.c.bind("<Button-5>", self.zoom)
        
        #self.c.bind()
        
        self.c.pack()
        
        #self.sizefac = math.sqrt(ParticleManager.SOLAR_MASS) * Particle.COLLISION_RADIUS_FACTOR / 500
        
        self.startx = 0
        self.starty = 0
        
        self.dx = 0
        self.dy = 0
        self.clicked = False
        
        self.s = Semaphore(1)       
        self.run()
    
    
    def run(self):
        self.pm = ParticleManager.ParticleManager(self)
        mainloop()
        
    def addParticle(self, particle):
        radius = math.sqrt(Particle.COLLISION_RADIUS_FACTOR * particle.mass)
        if radius < 1:
            radius = 1
        self.c.delete(particle.canvas)
        particle.canvas = self.c.create_oval(SIZE/2.0 + particle.pos[0] - radius, SIZE/2.0 + particle.pos[1] - radius, SIZE/2.0 + particle.pos[0] + radius, SIZE/2.0 + particle.pos[1] + radius, fill = "black")


   
    def startmove(self, event):
        self.startx = event.x - self.dx
        self.starty = event.y - self.dy
        self.clicked = True
    
    def move(self, event):
        if self.clicked:
            self.dx = - self.startx + event.x
            self.dy = - self.starty + event.y
    
    #def submit_to_tk(self, callablef, *args, **kwargs):
    #    self.request_queue.put_nowait((callablef, args, kwargs))
    #    try:
    #        return self.result_queue.get_nowait()
    #    except:
    #        return
            
    #def timertick(self, level = 0):
    #    #print self.request_queue.empty()
    #    try:
    #        callablef, args, kwargs = self.request_queue.get_nowait()
    #    except Queue.Empty:
    #        pass
    #    else:
    #        #print "something in queue"
    #        retval = callablef(*args, **kwargs)
    #        self.result_queue.put_nowait(retval)
    #    if not self.request_queue.empty(): self.timertick(level + 1)
    #    if level == 0:
    #        self.master.after(1, self.timertick)
    def endmove(self, event):
        self.clicked = False
        
    def zoom(self, event):
        if event.num == 5 or event.delta == -120:
            self.pm.faktor *= 1.1
        else:
            self.pm.faktor /= 1.1
        
        
if __name__ == '__main__':   
    g = GUI()