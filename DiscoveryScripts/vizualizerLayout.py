from vpython import *
from numpy import * 

w=1320
h=650
axis = False

# VPython axis orientation
arrow_scalar = 2
x_vector = vector(arrow_scalar,0,0)
y_vector = vector(0,arrow_scalar,0)
z_vector = vector(0,0,arrow_scalar)

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
    if evt.checked:
        x_axis.visible = True
        x_lbl.visible = True
        y_axis.visible = True
        y_lbl.visible = True
        z_axis.visible = True
        z_lbl.visible = True
    else:
        x_axis.visible = False
        x_lbl.visible = False
        y_axis.visible = False
        y_lbl.visible = False
        z_axis.visible = False
        z_lbl.visible = False

x_axis = arrow(center=vector(0,0,0),axis=vector(2,0,0),color=color.green,shaftwidth=0.01,round=True,visible=True)
x_lbl = label(pos=vector(2,0,0),text='X',color=color.green,box=False)
x_axis.rotate(origin=vector(0,0,0),axis=y_vector,angle=-pi/2)
x_lbl.rotate(origin=vector(0,0,0),axis=y_vector,angle=-pi/2)

y_axis = arrow(center=vector(0,0,0),axis=vector(0,2,0),color=color.red,shaftwidth=0.01,round=True,visible=True)
y_lbl = label(pos=vector(0,2,0),text='Y',color=color.red,box=False)
y_axis.rotate(origin=vector(0,0,0),axis=x_vector,angle=-pi/2)
y_lbl.rotate(origin=vector(0,0,0),axis=x_vector,angle=-pi/2)
y_axis.rotate(origin=vector(0,0,0),axis=y_vector,angle=-pi/2)
y_lbl.rotate(origin=vector(0,0,0),axis=y_vector,angle=-pi/2)

z_axis = arrow(center=vector(0,0,0),axis=vector(0,0,2),color=color.blue,shaftwidth=0.01,round=True,visible=True)
z_lbl = label(pos=vector(0,0,2),text='Z',color=color.blue,box=False)
z_axis.rotate(origin=vector(0,0,0),axis=x_vector,angle=-pi/2)
z_lbl.rotate(origin=vector(0,0,0),axis=x_vector,angle=-pi/2)
    
my_box = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.red,canvas=screen)


screen.append_to_caption('Screen Size ')
menu(choices=['1320x650' ,'760x325'], bind=screen_size,pos=screen.caption_anchor)

    
screen.append_to_caption('\n\n\n')
chk_axises = checkbox(text='Show X,Y,Z Axis',bind=manage_axises,pos=screen.caption_anchor,checked=True)

screen.append_to_caption('\n\n\n')
screen.append_to_caption('Change animation speed!\n')
dec_speed = button(bind=increment_speed,text='Decrease Time', pos=screen.caption_anchor,background=color.blue)
real_speed = button(bind=increment_speed,text='Real Time', pos=screen.caption_anchor,background=color.blue)
inc_speed = button(bind=increment_speed,text='Increase Time',pos=screen.caption_anchor,background=color.blue)


while True:
    pass