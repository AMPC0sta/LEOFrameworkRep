from vpython import *
from numpy import *
from visualizerParameters import VisualizerParameters
from coordinateSystem import *


width=1320
height=650
main_title = 'Orbit Visualizer'

parameters = VisualizerParameters()
screen = canvas(width=(width*4/5)-50,height=height,align='left',title=main_title)
l = parameters.e_radius
print(l)
c = CoordinateSystem(lenght=l)
print(c.angle)
c.transform_from_vpython_to_ecef()

while True:
    pass

