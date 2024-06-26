from vpython import *

class SatelliteRepresentation:
    
    def __init__(self,space=canvas(title='Default'),size = vector(500,500,500),pos=vector(0,0,0)):
        self.space=space
        self.pos = pos
        self.size = size
        
        # Create satellite body (cylinder)
        self.satellite_body = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1e3), radius=5e2, color=color.red,canvas = self.space)

        # Create satellite solar panels (planes)
        self.panel1 = box(pos=vector(1.4e3, 0, 5e2), size=vector(2e3, 0.8e3, 0.1e3), color=color.gray(0.5),canvas=self.space)
        self.panel2 = box(pos=vector(-1.4e3, 0, 5e2), size=vector(2e3, 0.8e3, 0.1e3), color=color.gray(0.5),canvas=self.space)

        # Create satellite antenna
        self.antenna = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 2e3), radius=0.05e3, color=color.blue,canvas=self.space)


        # Group components into a single compound object
        self.satellite = compound([self.satellite_body, self.panel1, self.panel2, self.antenna],canvas=self.space)
        self.satellite.size = self.size

        # Set initial position of the satellite
        self.satellite.pos = self.pos


    def set_position(self,pos):
        self.pos = pos
        sat = self.satellite
        sat.pos = self.pos
        self.satellite = sat
    
        
    def set_size(self,size):
        self.size = size
        self.satellite.size = self.size
        
    def get_size(self):
        return self.size
    
    def get_position(self):
        return self.pos


#sat = SatelliteRepresentation()

#while True:
#    pass