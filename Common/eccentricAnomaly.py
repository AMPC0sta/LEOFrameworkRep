
from math import *

class EccentricAnomaly:
    # Determine the eccentric anomaly of a given mean anomaly for a given eccentric and epoch
    # convergeence parameter is initiated as 10e-6 rads, but can be set in: 
    
    # Kepler's equation M = E - e sin(E) to be solved through Newton-Rapshon iterative method.
    
    default_tolerance = 0.000001 # Tolerance set for convergeence determination in rads
    
    def __init__(self,mean_anomaly,eccentricity,tolerance=None):
        global default_tolerance
        
        self.mean_anomaly = mean_anomaly
        self.eccentricity = eccentricity
        
        if tolerance == None:
            self.tolerance = default_tolerance
        else:
            self.tolerance = tolerance
        
    
    def set_tolerance(self,tolerance):
        self.tolerance = tolerance
        
        
    def get_tolerance(self):
        return self.tolerance
    
    
    def set_mean_anomaly(self,mean_anomaly):
        self.mean_anomaly = mean_anomaly
        

    def get_mean_anomaly(self):
        return self.mean_anomaly
    
    
    def set_eccentricity(self,eccentricity):
        self.eccentricity = eccentricity
        
        
    def get_eccentricity(self):
        return self.eccentricity
    
    
    # Keppler equation for eccentric anomaly in order to E (eccentric anomaly)
    def e_anomaly_kepler_equation(self,E):
        return E - self.get_eccentricity() * sin(E) - self.get_mean_anomaly()
    
    
    # First derivative of Keppler equation for eccentric anomaly in order to E (eccentric anomaly)
    def e_anomaly_kepler_equation_fst_derivative(self,E):
        return 1 - self.get_eccentricity() * cos(E)
    
    
    def iteration_step(self,E):
        return E - self.e_anomaly_kepler_equation(E)/self.e_anomaly_kepler_equation_fst_derivative(E)
    
    
    
    
    
    