from math import *

class OrbitalMechanics:
    
    G = 6.6743e-11 #m3/kg*s2
    Me = 5.972e24 # kg
    earth_radius = 6371 #km
    seconds_per_day = 86400 # s
    
    def __init__(self,G=None,Me=None,earth_radius=None):
        
        if G == None:
            self.G = OrbitalMechanics.G
        else:
            self.G = G
        
        if Me == None:    
            self.Me = OrbitalMechanics.Me
        else:
            self.Me = Me
            
        self.miu = self.G * self.Me
        
        if earth_radius == None:
            self.earth_radius = OrbitalMechanics.earth_radius
        else:
            self.earth_radius = earth_radius

    
    def get_miu(self):
        return self.miu


    def calculate_semi_major_axis_a(self,mean_motion):
        # a = (miu/n^2)^(1/3)
        n = mean_motion * 2 * pi/ OrbitalMechanics.seconds_per_day
        
        return (self.get_miu()/n**2) ** (1/3)
    

    # redial distance is no more than altitude, v stands for the true anomaly of eccentricity e and mean_anomaly and mean_motion
    def calculate_redial_distance(self,eccentricity,true_anomaly,mean_motion):
        #r = (a(1-e^2))/(1+e*cos(v))
        
        a = self.calculate_semi_major_axis_a(mean_motion=mean_motion)
        
        d = a * ( 1 - eccentricity**2)
        n = ( 1 + eccentricity * cos(true_anomaly))
        
        return d/n
    
    
    # coordinates of orbital plane
    def calculate_coordinates_on_orbital_plane(self,true_anomaly,redial):
        
        p = redial * cos (true_anomaly)
        q = redial * sin (true_anomaly)
        
        return (p,q)