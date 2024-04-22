from vpython import *
from numpy import *
from visualizerParameters import VisualizerParameters
from coordinateSystem import CoordinateSystem


width=1320
height=650
main_title = 'Orbit Visualizer'

parameters = VisualizerParameters(7000)
screen = canvas(width=(width*4/5)-50,height=height,align='left',title=main_title)
coords = CoordinateSystem(None,None,parameters.e_radius)



while True:
    pass

