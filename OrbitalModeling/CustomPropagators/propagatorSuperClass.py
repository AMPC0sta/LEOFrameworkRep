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
    
    anomalies = None
    default_tolerance = 0.00000001
    
    def __init__(self,M,e,O,o,i,epoch):
        global default_tolerance, anomalies
        
        self.M = M
        self.e = e
        self.O = O
        self.o = O
        self.i = i
        self.epoch = epoch
        
        anomalies = Anomalies(mean_anomaly=M,eccentricity=e,tolerance=default_tolerance)
        self.E = anomalies.solve_eccentric_anomaly()
    
    
    @abstractmethod
    def propagate():
        pass