from vpython import *

class EarthModel:
 
    def __init__(self,earth_center=vector(0,0,0),radius=6371,canvas=canvas()):
        self.earth_center=earth_center
        self.radius=radius
        self.canvas = canvas
        
        self.earth=sphere(canvas=self.canvas,pos=self.earth_center,radius=self.radius,texture=textures.earth,shininess=0)
        self.canvas.lights=[]
        self.canvas.lights.append(distant_light(direction=vector(-1,0,0)))
        self.canvas.ambient=color.white*0.5
    
    def inclination(self,angle):
        self.tilt = angle
        self.earth.rotate(origin=self.earth_center,axis=vector(0,0,1),angle=self.tilt)     #Drawing earth inclination over Z axis
        
        