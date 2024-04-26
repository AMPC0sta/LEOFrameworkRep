from vpython import *
from numpy import *
from visualizerParameters import VisualizerParameters
from coordinateSystem import *
from earthModel import EarthModel

width=1320
height=650
main_title = 'Orbit Visualizer'

parameters = VisualizerParameters()
screen = canvas(width=(width*4/5)-50,height=height,align='left',title=main_title)
l = parameters.e_radius
print(l)
c = CoordinateSystem(lenght=l)
c.transform_from_vpython_to_ecef()

earth = EarthModel(canvas=screen,radius=l)

while True:
    pass

