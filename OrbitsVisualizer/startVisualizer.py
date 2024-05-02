from vpython import *
from numpy import *
import datetime 
from time import *
import sys
import os

# Move backwards on directory tree to allow to import custom modules from others folders
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from visualizerParameters import VisualizerParameters
from coordinateSystem import *
from earthModel import EarthModel
from Common.celestrakObjects import *   

# Global main settings
width=1320
height=650

screen_sizes = ['1320x650','1800x850']

main_title = 'Orbit Visualizer'
tilt = 23.5
dt = 0.01
real_dt = dt

# seconds on a day (non sidereal day)
# 360 º anomaly state earth full rotation (day)
day_secs = 24 * 60 * 60

# Auxiliary variables
e_rotation = False
selected_satellite = None
start_time = None
end_time = None
satellite = None


# Starting graphical objects
screen = canvas(width=(width*4/5)-50,height=height,align='left',title='<b>'+main_title+'</b>')
parameters = VisualizerParameters()
l = parameters.e_radius
c = CoordinateSystem(lenght=l,screen=screen)
# load available TLE objects on Celestrak website
satellites_db = CelestrakObjects()



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
    
    
def manage_satellite(m):
    global selected_satellite
    
    selected_satellite = m.selected
    if selected_satellite != None:
        satellites_db.pick_one_sat(selected_satellite)
    
        current_time = datetime.datetime.now()
        start_time = current_time - datetime.timedelta(hours=12)
        end_time = current_time + datetime.timedelta(hours=12)
    
        motion_points = satellites_db.get_orbits(start_time,end_time)
        #(x,y,z,t) = c.transform_4d_point(motion_points[0])
        #satellites = sphere(pos=
    
    

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

    
def manage_speed(evt):
    global dt
    if evt.text == 'Increase Time':
        dt = 1.1 * dt
    if evt.text == 'Decrease Time':
        dt = 0.9 * dt
    if evt.text == 'Real Time':
        dt = real_dt


# Coordinates systems set and earth inclination    
c.transform_from_vpython_to_ecef()
earth = EarthModel(canvas=screen,radius=l)
earth.inclination(23.5 * pi/180)
c.inclination(angle=23.5 * pi/180)


# Drawing interface controls
screen.append_to_caption('<p style="font-size:30px"><b>Visualizer Controls</b></p>\n<b>__________________ Graphic Interface __________________\n</b>')
screen.append_to_caption('Screen Sizes')
menu_sizes = menu(choices=screen_sizes,bind=select_screen_size,pos=screen.caption_anchor)
screen.append_to_caption('\n')
chk_axises = checkbox(text='Show X,Y,Z Axis',bind=manage_axises,pos=screen.caption_anchor,checked=True)
screen.append_to_caption('\n')
chk_poles = checkbox(text='Show North & South Poles',bind=manage_poles,pos=screen.caption_anchor,checked=False)


screen.append_to_caption('\n\n<b>____________________ Environment ____________________</b>\n')
screen.append_to_caption('Slide to obtain inclination angle: \n')
tilt_slider = slider(bind=manage_tilt,min=-23.5,max=23.5,value=23.5,step=0.1,id='Tilt')
stext = wtext(text=str(tilt_slider.value)+ " º",canvas=screen,pos=screen.caption_anchor)

screen.append_to_caption('\n\n')
chk_rotation = checkbox(text='Enable Earth rotation!',bind=manage_e_rotation,pos=screen.caption_anchor,checked=False)
screen.append_to_caption('\n\nManage time delta\n')

dec_speed = button(bind=manage_speed,text='Decrease Time',pos=screen.caption_anchor,canvas=screen)
real_speed = button(bind=manage_speed,text='Real Time',pos=screen.caption_anchor,canvas=screen)
inc_speed = button(bind=manage_speed,text='Increase Time',pos=screen.caption_anchor,canvas=screen)

screen.append_to_caption('\n\n<b>___________________ Load Orbits _____________________</b>\n')
list = satellites_db.satellites_list
menu_sat = menu(text="Load satellite orbit",choices=list,bind=manage_satellite,pos=screen.caption_anchor,canvas=screen)
screen.append_to_caption('\n\n<b>____________________ Dashboard ______________________</b>\n')

elapsed_text = wtext(text='Time elapsed = 0 sec',canvas=screen)
screen.append_to_caption('\n')
elapsed_angle_text = wtext(text='Earth rotation anomaly = 0 º',canvas=screen)
screen.append_to_caption('\n')
time_of_the_day = wtext(text='Time of the day = 00:00:00',canvas=screen)
screen.append_to_caption('\n\n<b>___________________________________________________</b>\n')
screen.append_to_caption('Use mouse scroll wheel to zoom in/out!\n')
screen.append_to_caption('Use mouse right button to change camera position\n')



# Temporal buckets (to be changed to allig with UTC, and seasonal daylight)
t = 0
ptr = 0
earth_anomaly = 0
dt_i = datetime.datetime.now()

while True:
    rate(60)   # Allow 60 animation frames iteration per second
    
    t = t  + dt
    ptr = ptr + 1
    
    if ptr==60:
        dt_a = datetime.datetime.now()
        tmp = dt_a - dt_i
        elapsed_text.text = 'Time Elapsed = ' + str(tmp) + ' secs.'
        ptr=0
    
    if e_rotation == True:
        earth.earth_rotation(dt)
        if earth_anomaly > 2 * pi:
            earth_anomaly = 0
        
        secs = earth_anomaly * day_secs/(2*pi)
        time_of_the_day.text = 'Time of the day = ' + strftime("%H:%M:%S", gmtime(secs))

        earth_anomaly = earth_anomaly + mag(earth.angular_velocity) * dt
        elapsed_angle_text.text= 'Earth rotation anomaly = ' + str(round(earth_anomaly*180/pi,3))  + ' º'

    

