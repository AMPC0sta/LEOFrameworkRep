from vpython import *
from numpy import *

w=1320
h=650

screen = canvas(width=(w*4/5)-50,height=h,align='left',title='Orbit Visualizer')

def screen_size(m):
    if m.selected == "1320x650":
        w = 1320
        h = 650
    elif m.selected == "760x325":
        w=760
        h=325
    screen.width = (w*4/5)-50
    screen.height = h
    
# buttons
def increment_speed(evt):
    global dt
    if evt.text == 'Increase Time':
        #dt = 1.1 * dt
        print('pressed!')
    if evt.text == 'Decrease Time':
        #dt = 0.9 * dt
        print('pressed!')
    if evt.text == 'Real Time':
        #dt = real_dt
        print('pressed!')

def manage_axises(evt):
    global axis 
    if evt.checked:
        axis = True
    else:
        axis = False

my_box = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.red,canvas=screen)

screen.append_to_caption('Screen Size ')
menu(choices=['1320x650' ,'760x325'], bind=screen_size,pos=screen.caption_anchor)

    
screen.append_to_caption('\n\n\n')
chk_axises = checkbox(text='Show X,Y,Z Axis',bind=manage_axises,pos=screen.caption_anchor,checked=False)

screen.append_to_caption('\n\n\n')
screen.append_to_caption('Change animation speed!\n')
dec_speed = button(bind=increment_speed,text='Decrease Time', pos=screen.caption_anchor,background=color.blue)
real_speed = button(bind=increment_speed,text='Real Time', pos=screen.caption_anchor,background=color.blue)
inc_speed = button(bind=increment_speed,text='Increase Time',pos=screen.caption_anchor,background=color.blue)




while True:
    pass