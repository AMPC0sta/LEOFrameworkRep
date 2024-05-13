from vpython import *

class CoordinateSystem:


    # axis colors and global definitions setup
    x_axis_color = color.blue
    y_axis_color = color.red
    z_axis_color = color.yellow
    axis_shaft = 50
    
    
    def __init__(self,type='ecef',center=vector(0,0,0),lenght=1,angle=0,visible=True,screen=canvas()):
        # Internal state
        self.type = type
        self.center = center
        self.lenght = lenght *1.1
        self.angle = angle * pi/180
        self.screen = screen
        
        # Max lenght in vectorial way
        self.x_vector = 1.3 * vector(self.lenght,0,0)
        self.y_vector = 1.3 * vector(0,self.lenght,0)
        self.z_vector = 1.3 * vector(0,0,self.lenght)
        
        # Norm vectors (to act as rotation pivot's)
        self.rot_axis_x = vector(1,0,0)
        self.rot_axis_y = vector(0,1,0)
        self.rot_axis_z = vector(0,0,1)
        
        # Drawing system
        self.x_axis = arrow(canvas=self.screen,center=self.center,axis=self.x_vector,color=CoordinateSystem.x_axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True,visible=True)
        self.x_lbl = label(canvas=self.screen,pos=self.x_vector,text='X',color=CoordinateSystem.x_axis_color,box=False)

        self.y_axis = arrow(canvas=self.screen,center=self.center,axis=self.y_vector,color=CoordinateSystem.y_axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True)
        self.y_lbl = label(canvas=self.screen,pos=self.y_vector,text='Y',color=CoordinateSystem.y_axis_color,box=False)

        self.z_axis = arrow(canvas=self.screen,center=self.center,axis=self.z_vector,color=CoordinateSystem.z_axis_color,shaftwidth=CoordinateSystem.axis_shaft,round=True)
        self.z_lbl = label(canvas=self.screen,pos=self.z_vector,text='Z',color=CoordinateSystem.z_axis_color,box=False)
          
           
        def get_space_axis(): 
            return (self.x_axis, self.y_axis, self.z_axis)
        
        
        def get_space_axis_labels():
            return (self.x_lbl,self.y_lbl,self.z_lbl)
        
        
    def visibility(self,state):
        self.state = state
        self.x_axis.visible = self.state
        self.x_lbl.visible = self.state
        
        self.y_axis.visible = self.state
        self.y_lbl.visible = self.state

        self.z_axis.visible = self.state
        self.z_lbl.visible = self.state


    def read_coordinates_visibility(self):
        return self.state
        
    # VPython axis order are Y,Z,X instead of X,Y,Z so that a transformation is needed to the axis    
    def transform_from_vpython_to_ecef(self):
        self.angle = pi/2

        self.x_axis.rotate(origin=self.center,axis=self.rot_axis_y,angle=-1*self.angle)
        self.x_lbl.rotate(origin=self.center,axis=self.rot_axis_y,angle=-1*self.angle)

        self.y_axis.rotate(origin=self.center,axis=self.rot_axis_z,angle=-1*self.angle)
        self.y_lbl.rotate(origin=self.center,axis=self.rot_axis_z,angle=-1*self.angle)

        self.z_axis.rotate(origin=self.center,axis=self.rot_axis_x,angle=-1*self.angle)
        self.z_lbl.rotate(origin=self.center,axis=self.rot_axis_x,angle=-1*self.angle)
        
        
    def inclination(self,angle):
        self.angle = angle
        
        self.z_axis.rotate(origin=self.center,axis=self.rot_axis_z,angle=self.angle)
        self.z_lbl.rotate(origin=self.center,axis=self.rot_axis_z,angle=self.angle)

        self.y_axis.rotate(origin=self.center,axis=self.rot_axis_z,angle=self.angle)
        self.y_lbl.rotate(origin=self.center,axis=self.rot_axis_z,angle=self.angle)


    def transform_4d_point(self,points,o_system,t_system):
        (x,y,z,t) = points
    
        if o_system == 'vpyton' and t_system == 'ecef':
            return (z,y,x,t)
        
        return points