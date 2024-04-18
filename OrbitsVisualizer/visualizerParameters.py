from numpy import *
from vpython import *

class VisualizerParameters:
    
    # Constructor
    def __init__(self,*args):
        if len(args)==3:
            self.e_radius = args[0]
            self.e_tilt = args[1]    
            self.e_center = args[2]
        elif len(args)==2:
            self.e_radius = args[0]
            self.e_tilt = args[1]    
            self.e_center = vector(0,0,0)
        elif len(args)==1:
            self.e_radius = args[0]
            self.e_tilt = (23 + 23/60) *  pi/180
            self.e_center = vector(0,0,0)
        else:
            self.e_radius = 6371
            self.e_tilt = (23 + 23/60) *  pi/180
            self.e_center = vector(0,0,0)
    
        

            
