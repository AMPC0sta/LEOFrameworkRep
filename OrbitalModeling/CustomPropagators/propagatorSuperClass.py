from abc import ABC, abstractmethod
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Common.anomalies import Anomalies
from Common.orbitalMechanics import OrbitalMechanics

class PropagatorSuperClass(ABC):
    
    # Orbital Parameters, extracted from Orbital Elements, loaded from TLE's
    # Satellite Name
    # Mean Anomaly (M)
    # Eccentricity (e)
    # Right Ascenscion of the Ascending Node (O)
    # Argument of Perigee (o)
    # iniclination (i)
    # Epoch
    
    # Intermediate needed variables
    # Eccentricty Anomaly (E)
    # True Anomaly (ta)
    
    # Derived Results (for initial boundaries conditions)
    # Cartesian Position Vector (r) => (rx,ry,rz)
    # Cartesian Velocity vector(v) => (vx,vy,vz)
    
    
    def __init__(self,M,e,O,o,i,epoch):
        self.M = M
        self.e = e
        self.O = O
        self.o = O
        self.i = i
        self.epoch = epoch
    
    
    @abstractmethod
    def propagate():
        pass