from vpython import *
from numpy import *
from datetime import *

from visualizerParameters import VisualizerParameters
from coordinateSystem import *
from earthModel import EarthModel



# Global main settings
width=1320
height=650

screen_sizes = ['1320x650','1800x850']

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

def select_screen_size(m):
    global width, height

    if m.selected == screen_sizes[0]:
        width = 1320
        height = 650
    if m.selected == screen_sizes[1]:
        width = 1800
        height = 850
    
    screen.width = (width * 4/5) - 50
    screen.height = height

def manage_axises(event):
    if event.checked:
        c.visibility(True)
        earth.poles_visibility(False)
        chk_poles.checked = False
            
    else:
        c.visibility(False)
        
def manage_poles(event):
        if event.checked:
            earth.poles_visibility(True)
            c.visibility(False)
            chk_axises.checked = False

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
screen.append_to_caption('Visualizer Controls\n_____________________ Graphic Interface ____________________\n')
screen.append_to_caption('Screen Sizes')
menu_sizes = menu(choices=screen_sizes,bind=select_screen_size,pos=screen.caption_anchor)
screen.append_to_caption('\n')
chk_axises = checkbox(text='Show X,Y,Z Axis',bind=manage_axises,pos=screen.caption_anchor,checked=True)
screen.append_to_caption('\n')
chk_poles = checkbox(text='Show North & South Poles',bind=manage_poles,pos=screen.caption_anchor,checked=False)


screen.append_to_caption('\n\n_______________________ Environment ______________________\n')
screen.append_to_caption('Slide to obtain inclination angle: \n')
tilt_slider = slider(bind=manage_tilt,min=-23.5,max=23.5,value=23.5,step=0.1,id='Tilt')
stext = wtext(text=str(tilt_slider.value)+ " º",canvas=screen,pos=screen.caption_anchor)

screen.append_to_caption('\n\n')
chk_rotation = checkbox(text='Enable Earth rotation!',bind=manage_e_rotation,pos=screen.caption_anchor,checked=False)
screen.append_to_caption('\n\n________________________________________________________\n')
elapsed_text = wtext(text='Time elapsed = 0 sec',canvas=screen)
screen.append_to_caption('\n')
elapsed_angle_text = wtext(text='Earth rotation anomaly = 0 º',canvas=screen)
screen.append_to_caption('\n\n________________________________________________________\n')
screen.append_to_caption('Use mouse scroll wheel to zoom in/out!\n')
screen.append_to_caption('Use mouse right button to change camera position\n')



# Temporal buckets (to be changed to allig with UTC, and seasonal daylight)
dt = 0.01 
t = 0
ptr = 0
earth_anomaly = 0
dt_i = datetime.now()

while True:
    rate(60)   # Allow 60 animation frames iteration per second
    
    t = t  + dt
    ptr = ptr + 1
    
    if ptr==60:
        dt_a = datetime.now()
        tmp = dt_a - dt_i
        elapsed_text.text = 'Time Elapsed = ' + str(tmp) + ' secs.'
        ptr=0
    
    if e_rotation == True:
        earth.earth_rotation(dt)
        if earth_anomaly > 2 * pi:
            earth_anomaly = 0
            
        earth_anomaly = earth_anomaly + mag(earth.angular_velocity) * dt
        elapsed_angle_text.text= 'Earth rotation anomaly = ' + str(round(earth_anomaly*180/pi,3))  + ' º'

    

