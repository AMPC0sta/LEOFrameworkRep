from vpython import *

#set_browser(type='pyqt')

# Create two canvases
canvas1 = canvas(title='Left Canvas', width=400, height=400)
canvas2 = canvas(title='Right Canvas', width=400, height=400)

# Set the positions of the canvases to position them side by side
canvas1.pos = vector(-400, 0, 0)
canvas2.pos = vector(400, 0, 0)

# Create objects in the left canvas
canvas1.select()
sph=sphere(pos=vector(-1, 0, 0), radius=1, color=color.red)
clr=cylinder(pos=vector(-2, -1, 0), axis=vector(0, 2, 0), radius=0.5, color=color.green)

# Create objects in the right canvas
canvas2.select()
bx=box(pos=vector(1, 0, 0), size=vector(1, 1, 1), color=color.blue)
ar=arrow(pos=vector(2, 0, 0), axis=vector(1, 1, 0), color=color.yellow)

# Adjust the camera for better visualization
scene.center = vector(0, 0, 0)
scene.autoscale = False


while True:
    pass