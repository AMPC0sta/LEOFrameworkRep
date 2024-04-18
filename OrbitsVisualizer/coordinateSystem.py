from vpython import *

class CoordinateSystem:

    axis_color = color.green
    axis_shaft = 0.01
    

    def __init__(self,type,lenght,angle,visible):
        if type == None:
            self.type = 'ecef'
        else:
            self.type = type
            
        self.center = vector(0,0,0)
        
        if lenght == None:
            self.lenght = 1
        else:
            self.lenght = lenght
        
        if angle == None:
            self.angle = 0
        else:
            self.angle = angle
        
        if visible == None:
            self.visible = True
        else:
            self.visible = visible
            
        self.x_axis = arrow(center=self.center,axis=vector(self.lenght,0,0),color=CoordinateSystem.axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True,visible=self.visible)
        self.x_lbl = label(pos=vector(self.lenght,0,0),text='X',color=CoordinateSystem.axis_color=False)

        self.y_axis = arrow(center=self.center,axis=vector(0,self.lenght,0),color=CoordinateSystem.axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True,visible=self.visible)
        self.y_lbl = label(pos=vector(0,self.lenght,0),text='Y',color=CoordinateSystem.axis_color=False)

        self.z_axis = arrow(center=self.center,axis=vector(0,0,self.lenght),color=CoordinateSystem.axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True,visible=self.visible)
        self.z_lbl = label(pos=vector(0,0,self.lenght),text='Z',color=CoordinateSystem.axis_color=False)

        def get_space_axis(): 
            return (self.x_axis, self.y_axis, self.z_axis)
        
        def get_space_axis_labels():
            return (self.x_lbl,self.y_lbl,self.z_lbl)
        
        
        