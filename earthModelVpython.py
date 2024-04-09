# Tutorial = https://www.youtube.com/watch?v=lQ5epHnu0j8

from vpython import *
from numpy import *

#Simulation parameters
earth_r = 1
earth_center = vector(0,0,0)
tilt = 23.5*pi/180
lat = 30*pi/180
t = 0
dt = 0.01

scene = canvas(title="ISS Orbit", width=1520, height=700)
lbl = label(pos=vector(-4.5,0,0),text='Time = 0',box=False)

#Earth
earth=sphere(pos=earth_center,radius=earth_r,texture=textures.earth,shininess=0)
scene.lights=[]
scene.lights.append(distant_light(direction=vector(-1,0,0)))
scene.ambient=color.white*0.5
earth.rotate(origin=earth_center,axis=vector(0,0,1),angle=tilt)     #Drawing earth inclination over Z axis

npole = cylinder(pos=earth_center,axis=1.5*earth_r*vector(-sin(tilt),cos(tilt),0),radius=0.01*earth_r)
spole = cylinder(pos=earth_center,axis=-1.5*earth_r*vector(-sin(tilt),cos(tilt),0),radius=0.01*earth_r)

#point on earth
ball = sphere(pos=earth_r*vector(-cos(lat),sin(lat),0),radius=0.03,color=color.yellow,make_trail=False )
ball.rotate(origin=earth_center,axis=vector(0,0,1),angle=tilt)
#ball.make_trail=True

#vectorial angular velocity
w = 1*norm(npole.axis)

while t < 1000:
    rate(30)
    earth.rotate(origin=earth_center,axis=w,angle=mag(w)*dt)
    print(w)
    print(ball.pos)
    ball.v = w.cross(ball.pos)
    ball.pos = ball.pos + ball.v * dt
    t = t + dt
    lbl.text='Time = '+str(t)


