from vpython import *

class CoordinateSystem:

    x_axis_color = color.blue
    y_axis_color = color.red
    z_axis_color = color.yellow
    axis_shaft = 50
    
    def __init__(self,type='ecef',center=vector(0,0,0),lenght=1,angle=0,visible=True):
   
        self.type = type
        self.center = center
        self.lenght = lenght *1.1
        self.angle = angle * pi/180
        
        self.x_vector = 1.5 * vector(self.lenght,0,0)
        self.y_vector = 1.5 * vector(0,self.lenght,0)
        self.z_vector = 1.5 * vector(0,0,self.lenght)
        
        self.rot_axis_x = vector(1,0,0)
        self.rot_axis_y = vector(0,1,0)
        self.rot_axis_z = vector(0,0,1)
        
        self.x_axis = arrow(center=self.center,axis=self.x_vector,color=CoordinateSystem.x_axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True,visible=True)
        self.x_lbl = label(pos=self.x_vector,text='X',color=CoordinateSystem.x_axis_color,box=False)

        self.y_axis = arrow(center=self.center,axis=self.y_vector,color=CoordinateSystem.y_axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True)
        self.y_lbl = label(pos=self.y_vector,text='Y',color=CoordinateSystem.y_axis_color,box=False)

        self.z_axis = arrow(center=self.center,axis=self.z_vector,color=CoordinateSystem.z_axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True)
        self.z_lbl = label(pos=self.z_vector,text='Z',color=CoordinateSystem.z_axis_color,box=False)
           
        def get_space_axis(): 
            return (self.x_axis, self.y_axis, self.z_axis)
        
        
        def get_space_axis_labels():
            return (self.x_lbl,self.y_lbl,self.z_lbl)
        
        
    def transform_from_vpython_to_ecef(self):
        self.angle = pi/2

        self.x_axis.rotate(origin=self.center,axis=self.rot_axis_y,angle=self.angle)
        self.x_lbl.rotate(origin=self.center,axis=self.rot_axis_y,angle=self.angle)

        self.y_axis.rotate(origin=self.center,axis=self.rot_axis_z,angle=-1*self.angle)
        self.y_lbl.rotate(origin=self.center,axis=self.rot_axis_z,angle=-1*self.angle)

        self.z_axis.rotate(origin=self.center,axis=self.rot_axis_x,angle=-1*self.angle)
        self.z_lbl.rotate(origin=self.center,axis=self.rot_axis_x,angle=-1*self.angle)
            