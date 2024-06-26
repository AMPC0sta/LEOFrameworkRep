from vpython import *
from numpy import *
import datetime 
from time import *
import sys
import os
import ast

# Move backwards on directory tree to allow to import custom modules from others folders
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from visualizerParameters import VisualizerParameters
from coordinateSystem import *
from earthModel import EarthModel
from Common.celestrakObjects import *   
from satelliteRepresentation import *

# Global main settings
width=1320
height=650
sim_speed = 60  # 60 frames per second ( each frame correspond to one minute dt )
real_sim_speed = sim_speed
screen_sizes = ['1320x650','1800x850']

main_title = 'Orbit Visualizer'
tilt = 23.5
dt = 60
motion_points = []

running = True

# seconds on a day (non sidereal day)
# 360 º anomaly state earth full rotation (day)
day_secs = 24 * 60 * 60
day_min = 24 * 60

# Auxiliary variables
e_rotation = False
selected_satellite = None
start_time = None
end_time = None
satellite_on = False

external_motion_points = []
external_orbit = False

def read_tuples_from_file(filename):
    tuples_array = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove the newline character and split the line by commas
            line = line.strip()
            if line:  # Check if the line is not empty
                # Split the line by commas and convert each element to the appropriate type
                tuple_elements = eval(line)  # Using eval to parse the line as a tuple
                tuples_array.append(tuple(tuple_elements))  # Append the tuple to the array
    return tuples_array


if (len(sys.argv)) == 3:
    temp_file_path = sys.argv[1]
    period = float(sys.argv[2])
    # Read the contents of the temporary file
    
    external_motion_points = read_tuples_from_file(temp_file_path)
            
    external_orbit = True

# Starting graphical objects
screen = canvas(width=(width*4/5)-50,height=height,align='left',title='<b>'+main_title+'</b>')
parameters = VisualizerParameters()
l = parameters.e_radius
c = CoordinateSystem(lenght=l,screen=screen)
# load available TLE objects on Celestrak website
satellites_db = CelestrakObjects()

# Draw satellite
satellite = SatelliteRepresentation(space=screen)
satellite.set_size(size=vector(500,500,500))
satellite.visible = False


# satellite_1 and trail_1 were used to compare orbit with tilted and non tilted earth.
# Tilted orbits were also comapred with SGP4 on MATLAB Aerospace Toolbox, with the same TLE and to the same time frame.
#satellite_1 = SatelliteRepresentation(space=screen)
#satellite_1.set_size(size=vector(500,500,500))
#satellite_1.visible = False

trail = curve(canvas=screen,color=color.green)
#trail_1 = curve(canvas=screen,color=color.blue)

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
    global motion_points
    global satellite
    global screen
    global satellite_on
    global period

    if len(motion_points) == 0:
        motion_points =  []

    selected_satellite = m.selected

    if selected_satellite != None or external_orbit:
        satellites_db.pick_one_sat(selected_satellite)
    
        current_time = datetime.datetime.now()
        start_time = current_time - datetime.timedelta(hours=12)
        end_time = current_time + datetime.timedelta(hours=12)
    
        satellite_on = True
        period = satellites_db.get_object_period()
        
        motion_points = satellites_db.get_orbits(start_time,end_time)

        (x,y,z,t) = c.transform_4d_point(points=motion_points[0],o_system='vpython',t_system='ecef')
        p0 = parameters.e_radius * vector(x,y,z)
        (x,y,z,t) = c.rotate_earth_tilt(p0)
        p = (x,y,x,t)
        
        satellite.visible = True
        satellite.set_position(pos=vector(x,y,z))
        
        #satellite_1.visible = True
        #satellite_1.set_position(pos=p0)
        trail.append(p)
        #trail_1.append(p0)

        screen.title='<b>'+main_title+' ('+selected_satellite+')</b>'
        

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
    global sim_speed
    if evt.text == 'Increase Time':
        sim_speed = trunc(1.1 * sim_speed)
    if evt.text == 'Decrease Time':
        sim_speed = trunc(0.9 * sim_speed)
    if evt.text == 'Real Time':
        sim_speed = real_sim_speed


def quit_script(evt):
    global running
    
    running = False
    
    screen.delete()
    print("Script terminated gracefully.")
    
    

# Coordinates systems set and earth inclination    
c.transform_from_vpython_to_ecef()
earth = EarthModel(canvas=screen,radius=l)
earth.inclination(23.5 * pi/180)
c.inclination(angle=23.5 * pi/180)


# Drawing interface controls
screen.append_to_caption('<p style="font-size:25px"><b>Visualizer Controls</b></p>\n<b>__________________ Graphic Interface __________________\n</b>')
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

elapsed_text = wtext(text='Satellite Orbit Time elapsed = 0 min',canvas=screen)
screen.append_to_caption('\n')
elapsed_angle_text = wtext(text='Earth rotation anomaly = 0 º',canvas=screen)
screen.append_to_caption('\n')
time_of_the_day = wtext(text='Time of the day = 00:00:00',canvas=screen)
screen.append_to_caption('\n\n<b>___________________________________________________</b>\n')
screen.append_to_caption('Use mouse scroll wheel to zoom in/out!\n')
screen.append_to_caption('Use mouse right button to change camera position\n')
screen.append_to_caption('Listed satellites orbital parameters are placed on www.celestrak.org\n')
screen.append_to_caption('it may take a while to download!\n')
quit = button(bind=quit_script,text="Exit Program",pos=screen.caption_anchor,canvas=screen)


# Temporal buckets (to be changed to allig with UTC, and seasonal daylight)
t = 0
ptr = 0
earth_anomaly = 0
dt_i = datetime.datetime.now()
i = 0
#array_len  = motion_points.

# v = radius * w  --> tangential velocity from angular
# w = v/radius --> angular velocity from linear
# w = v * radius/radius = v rads/s --> because linear velocity is normalized 

if external_motion_points != []:
    motion_points = external_motion_points
    


while running:
    rate(sim_speed)   # Allow X animation frames iteration per second
    
    if e_rotation == True:
        earth.earth_rotation(dt)
        if earth_anomaly > 2 * pi:
            earth_anomaly = 0
            
        secs = earth_anomaly * day_secs/(2*pi)

        time_of_the_day.text = 'Time of the day = ' + strftime("%H:%M:%S", gmtime(secs))

        earth_anomaly = earth_anomaly + mag(earth.angular_velocity) * dt
        elapsed_angle_text.text= 'Earth rotation anomaly = ' + str(round(earth_anomaly*180/pi,3))  + ' º'
        
    if satellite_on or external_orbit:
        if ptr < period-1:
                if i < len(motion_points):
                    p0 = c.transform_4d_point(motion_points[i],'vpython','ecef')
                    (x,y,z,t1) = c.rotate_earth_tilt(p0)
                    satellite.set_position(pos=parameters.e_radius * vector(x,y,z))
                    #(x0,y0,z0,t0) = p0
                    #satellite_1.set_position(pos=parameters.e_radius * vector(x0,y0,z0))
                    trail.append(satellite.get_position())
                    #trail_1.append(satellite_1.get_position())
                    i = i + 1
                else:
                    i = 0
                
                elapsed_text.text='Satellite Orbit Time elapsed = ' + str(ptr) + ' mins'
                ptr = ptr + 1
        else:
            trail.clear()
            ptr = 0
