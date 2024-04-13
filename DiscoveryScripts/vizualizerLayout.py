from vpython import *
from numpy import *

w=1320
h=650

screen_left = canvas(width=(w/3)-10,height=h,align='left')
screen_right = canvas(width=(w*2/3)-10,height=h,align='right')

def screen_size(m):
    if m.selected == "1320x650":
        w = 1320
        h = 650
    elif m.selected == "760x325":
        w=760
        h=325
    screen_left.width = (w/3)-10
    screen_right.width = (w*2/3)-10

screen_left.select()
menu(choices=['1320x650' ,'760x325'], bind=screen_size,pos=screen_left.append_to_title())
my_box = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.red,canvas=screen_right)

while True:
    pass