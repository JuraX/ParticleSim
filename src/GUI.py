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
        #self.timertick()
        self.pm = ParticleManager(self)
        mainloop()
        
    def addParticle(self, particle):
        radius = math.sqrt(Particle.COLLISION_RADIUS_FACTOR * particle.mass)
        if radius < 1:
            radius = 1
        #self.submit_to_tk(self.c.create_oval, SIZE/2.0 + particle.pos[0] - radius, SIZE/2.0 + particle.pos[1] - radius, SIZE/2.0 + particle.pos[0] + radius, SIZE/2.0 + particle.pos[1] + radius, fill = "black")
        self.c.create_oval(SIZE/2.0 + particle.pos[0] - radius, SIZE/2.0 + particle.pos[1] - radius, SIZE/2.0 + particle.pos[0] + radius, SIZE/2.0 + particle.pos[1] + radius, fill = "black")
   
    def clearall(self):
        self.c.delete(ALL)
    
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

        
        
if __name__ == '__main__':   
    g = GUI()