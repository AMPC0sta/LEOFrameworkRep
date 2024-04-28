from vpython import *
from numpy import *
from visualizerParameters import VisualizerParameters
from coordinateSystem import *
from earthModel import EarthModel


# Global main settings
width=1320
height=650
main_title = 'Orbit Visualizer'
tilt = 23.5

# Auxiliary variables
e_rotation = False


# Starting graphical objects
screen = canvas(width=(width*4/5)-50,height=height,align='left',title=main_title)
parameters = VisualizerParameters()
l = parameters.e_radius
c = CoordinateSystem(lenght=l,screen=screen)


# Interface control events/management
def manage_axises(event):
    if event.checked:
        c.visibility(True)
        
        if chk_poles.checked:
            chk_poles.checked = False
            earth.poles_visibility(False)
    else:
        c.visibility(False)
        
def manage_poles(event):
        if event.checked:
            chk_axises.checked = False
            
            if chk_axises.checked:
                c.visibility(False)
                earth.poles_visibility(False)
        else:
            earth.poles_visibility(False)
        
def manage_tilt(event):
    global tilt
    global tmp_tilt
    if event.id == 'Tilt':
        tmp_tilt = event.value
        
        earth.inclination(angle=(tmp_tilt-tilt) * pi/180)
        c.inclination(angle=(tmp_tilt-tilt) * pi/180)
        tilt = tmp_tilt
        stext.text = str(event.value)+ " º"

def manage_e_rotation(event):
    global e_rotation 
    e_rotation = event.checked



# Coordinates systems set and earth inclination    
c.transform_from_vpython_to_ecef()
earth = EarthModel(canvas=screen,radius=l)
earth.inclination(23.5 * pi/180)
c.inclination(angle=23.5 * pi/180)


# Drawing interface controls
screen.append_to_caption('Visualizer Controls\n________________________________________________________\n')
chk_axises = checkbox(text='Show X,Y,Z Axis',bind=manage_axises,pos=screen.caption_anchor,checked=True)
screen.append_to_caption('\n')
chk_poles = checkbox(text='Show North & South Poles',bind=manage_poles,pos=screen.caption_anchor,checked=False)

screen.append_to_caption('\n\nSlide to obtain inclination angle: \n')
tilt_slider = slider(bind=manage_tilt,min=-23.5,max=23.5,value=23.5,step=0.1,id='Tilt')
stext = wtext(text=str(tilt_slider.value)+ " º",canvas=screen)

screen.append_to_caption('\n\n')
chk_poles = checkbox(text='Enable Earth rotation!',bind=manage_e_rotation,pos=screen.caption_anchor,checked=False)
screen.append_to_caption('\n\n________________________________________________________\n')
screen.append_to_caption('Use mouse scroll wheel to zoom in/out!\n')
screen.append_to_caption('Use mouse right button to change camera position\n')



# Temporal buckets (to be changed to allig with UTC, and seasonal daylight)
dt = 0.01 
t = 0

while True:
    rate(30)   # Allow 60 animation frames iteration per second
    
    t = t  + dt
    if e_rotation == True:
        earth.earth_rotation(dt)

    

