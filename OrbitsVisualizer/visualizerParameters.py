from numpy import *
from vpython import *

class VisualizerParameters:
    
    # Constructor
    def __init__(self,e_radius,e_tilt,e_center):
        
        if e_radius == None:
           self.e_radius = 6371 # Default Earth radius in km's
        else:
            self.e_radius = e_radius
        
        if e_tilt == None:
           self.e_tilt = (23 + 23/60) *  pi/180   # Default Earth axis tilt  (Z), 23 degrees plus 23 minutes of the arc converted into rads
        else:
            self.e_tilt = e_tilt
            
        if e_center == None:
            self.e_center = vector(0,0,0)
        else
            self.e_center = e_center
            
