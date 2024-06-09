
class EccentricAnomaly:
    # Determine the eccentric anomaly of a given mean anomaly for a given eccentric and epoch
    # convergeence parameter is initiated as 10e-6 rads, but can be set in: 
    
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
    
    