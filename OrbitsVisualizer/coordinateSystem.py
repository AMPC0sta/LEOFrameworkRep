from vpython import *

class CoordinateSystem:

    axis_color = color.green
    axis_shaft = 10
    

    def __init__(self,type='ecef',center=vector(0,0,0),lenght=1,angle=0,visible=True):
    
        self.type = type
        self.center = center
        self.lenght = lenght *1.5
        self.angle = angle
            
        self.x_axis = arrow(center=self.center,axis=vector(self.lenght,0,0),color=CoordinateSystem.axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True,visible=True)
        self.x_lbl = label(pos=vector(self.lenght,0,0),text='X',color=CoordinateSystem.axis_color,box=False)

        self.y_axis = arrow(center=self.center,axis=vector(0,self.lenght,0),color=CoordinateSystem.axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True)
        self.y_lbl = label(pos=vector(0,self.lenght,0),text='Y',color=CoordinateSystem.axis_color,box=False)

        self.z_axis = arrow(center=self.center,axis=vector(0,0,self.lenght),color=CoordinateSystem.axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True)
        self.z_lbl = label(pos=vector(0,0,self.lenght),text='Z',color=CoordinateSystem.axis_color,box=False)

        
        
        def get_space_axis(): 
            return (self.x_axis, self.y_axis, self.z_axis)
        
        
        
        def get_space_axis_labels():
            return (self.x_lbl,self.y_lbl,self.z_lbl)
        
        
        