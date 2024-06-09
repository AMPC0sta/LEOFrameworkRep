
from math import *

class EccentricAnomaly:
    # Determine the eccentric anomaly of a given mean anomaly for a given eccentric and epoch
    # convergeence parameter is initiated as 10e-6 rads, but can be set in: 
    
    # Kepler's equation M = E - e sin(E) to be solved through Newton-Rapshon iterative method.
    
    default_tolerance = 0.000001 # Tolerance set for convergeence determination in rads
    
    def __init__(self,mean_anomaly,eccentricity,tolerance=None):
        
        self.mean_anomaly = mean_anomaly
        self.eccentricity = eccentricity
        
        if tolerance == None:
            self.tolerance = EccentricAnomaly.default_tolerance
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
    
    
    def solve_eccentric_anomaly(self):
        #eccentricity is usually near 0, for LEO's, so that Mean Anomaly is a good aproximation for starting poing 
        
        # starting points
        E0 = self.get_mean_anomaly()
        E1 = E0 - self.e_anomaly_kepler_equation(E0)/self.e_anomaly_kepler_equation_fst_derivative(E0)
        
        # iterations
        while(abs(E1-E0) > self.get_tolerance()):
            E0 = E1
            E1 = E0 - self.e_anomaly_kepler_equation(E0)/self.e_anomaly_kepler_equation_fst_derivative(E0)
        
        return E1
        
#Testing function: for ma=2.0 and e=0.1 it is expectable to have 2.0869 rads.
def main():
    c = EccentricAnomaly(mean_anomaly=2.0,eccentricity=0.1)
    
    print("Eccentric Anomaly =", str(c.solve_eccentric_anomaly()))


#Testing  
if __name__ == "__main__":
    main()
    
    