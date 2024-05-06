from vpython import *

class SatelliteRepresentation:
    
    def __init__(self,canvas=canvas(),size=1,pos=vector(0,0,0)):
        self.canvas=canvas
        self.size = size
        self.pos = pos
        
        # Create satellite body (cylinder)
        self.satellite_body = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1e6), radius=5e5, color=color.red,canvas = self.canvas)

        # Create satellite solar panels (planes)
        self.panel1 = box(pos=vector(1.4e6, 0, 5e5), size=vector(2e6, 0.8e6, 0.1e6), color=color.gray(0.5),canvas=self.canvas)
        self.panel2 = box(pos=vector(-1.4e6, 0, 5e5), size=vector(2e6, 0.8e6, 0.1e6), color=color.gray(0.5),canvas=self.canvas)

        # Create satellite antenna
        self.antenna = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 2e6), radius=0.05e6, color=color.yellow,canvas=self.canvas)


        # Group components into a single compound object
        self.satellite = compound([self.satellite_body, self.panel1, self.panel2, self.antenna])

        # Set initial position of the satellite
        self.satellite.pos = self.pos
        self.satellite.size = self.satellite.size * self.size 

sat = SatelliteRepresentation()

while True:
    pass