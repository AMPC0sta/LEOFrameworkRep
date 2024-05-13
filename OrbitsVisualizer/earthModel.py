from vpython import *

class EarthModel:
 
    def __init__(self,earth_center=vector(0,0,0),radius=6371,canvas=canvas()):
        # Update object state
        self.earth_center=earth_center
        self.radius=radius
        self.canvas = canvas
        self.tilt = 0
        self.w = (2*pi)/(24*60*60)
        
        
        # Draw earth sphere, with world maps, and set lights from west
        self.earth=sphere(canvas=self.canvas,pos=self.earth_center,radius=self.radius,texture=textures.earth,shininess=0)
        self.canvas.lights=[]
        self.canvas.lights.append(distant_light(direction=vector(-1,0,0)))
        self.canvas.ambient=color.white*0.5
        
        # Draw earth poles but leave them invsible
        self.npole = cylinder(pos=self.earth_center,axis=1.5*self.radius*vector(-sin(self.tilt),cos(self.tilt),0),radius=0.01*self.radius,visible=False)
        self.spole = cylinder(pos=self.earth_center,axis=-1.5*self.radius*vector(-sin(self.tilt),cos(self.tilt),0),radius=0.01*self.radius,visible=False)
        
        self.angular_velocity = self.w*norm(self.npole.axis)
        
     
    def inclination(self,angle):
        self.tilt = angle
        
        # Give earth Z axis tilt
        self.earth.rotate(origin=self.earth_center,axis=vector(0,0,1),angle=self.tilt)     
        
        # Give poles the same tilt
        self.npole.rotate(origin=self.earth_center,axis=vector(0,0,1),angle=self.tilt)
        self.spole.rotate(origin=self.earth_center,axis=vector(0,0,1),angle=self.tilt)
        
        self.angular_velocity = self.w*norm(self.npole.axis)
    
    
        
    
    def poles_visibility(self,status):
        self.npole.visible=status
        self.spole.visible=status
        
    
    def read_poles_visibility(self):
        return self.npole.visible
        
        
    def earth_rotation(self,rotation_dt):
        self.rotation_dt = rotation_dt
        
        # Velocity per dt will determine the rotation anomaly
        self.earth.rotate(origin=self.earth_center,axis=self.angular_velocity,angle=mag(self.angular_velocity)*self.rotation_dt)
        