from vpython import *

class CoordinateSystem:

    axis_color = color.green
    axis_shaft = 10
    

    def __init__(self,*args):
        
        if len(args)==4:
            type = args[0]
            lenght = args[1]
            angle = args[2]
            visible = args[3]
        elif len(args)==3:
            type = args[0]
            lenght = args[1]
            angle = args[2]
            visible = None
        elif len(args)==2:
            type = args[0]
            lenght = args[1]
            angle = None
            visible = None
        elif len(args)==1:
            type = args[0]
            lenght = None
            angle = None
            visible = None
        else:
            type = None
            lenght = None
            angle = None
            visible = None
        
        if type == None:
            self.type = 'ecef'
        else:
            self.type = type
            
        self.center = vector(0,0,0)
        
        if lenght == None:
            self.lenght = 1
        else:
            self.lenght = lenght*1.5
        
        if angle == None:
            self.angle = 0
        else:
            self.angle = angle
        
        if visible == None:
            self.visible = True
        else:
            self.visible = visible
            
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
        
        
        