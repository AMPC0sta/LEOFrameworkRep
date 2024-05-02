from pyorbital import tlefile as tle_list
from pyorbital import orbital
import datetime

class CelestrakObjects:
    
    def __init__(self):
        self.satellites_list = []
        for node in tle_list.SATELLITES:
            self.satellites_list.append(node)
            
            
    def pick_one_sat(self,satellite):
        self.orbit = orbital.Orbital(satellite)
        
    def get_orbits(self,from_utc,to_utc):
        self.from_utc = from_utc
        self.to_utc = to_utc
        
        current_time = self.from_utc
        self.motion_position_points = []
        
        while current_time < to_utc:
            position,velocity = self.orbit.get_position(current_time)    # normalized position and velocity
            x,y,z = position
            point4D = (x,y,z,current_time)
            self.motion_position_points.append(point4D)
            current_time += datetime.timedelta(minutes=1)
        
        return self.motion_position_points