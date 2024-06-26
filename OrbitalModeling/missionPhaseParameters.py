from pyorbital.orbital import Orbital

import sys
import os

# Move backwards on directory tree to allow to import custom modules from others folders
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Common.orbitalElements import *

class MissionPhaseParameters:
    
    def __init__(self,phase_name=None,phase_position=0,tle_file = None):
        self.phase_name = phase_name
        self.tle_file = tle_file
        self.phase_position = phase_position
        self.orbital_elements = None
        self.start_datetime = None
        self.end_datetime = None
        self.motion_descriptor = None
    
    def read_object_name(self):
        if self.tle_file != None:
            
            
            # If TLE (Two Lines Element file has 3 lines (than consider first line as being satellite name), other wise satellite name is the filename)
            line = []
            with open(self.tle_file,'r') as f:
                for count,line in enumerate(f):
                    pass
            f.close()
            
            if count + 1 == 3:
                f = open(self.tle_file,'r')
                self.object_name = f.readline().strip()
                f.close()
            else:
                self.object_name = self.tle_file.split('\n')[len(self.tle_file.split)]
        else:
            raise RuntimeError("There's no TLE file set, for this mission phase!")

    def get_phase_name(self):
        return self.phase_name

    def load_TLE_data(self):
        self.read_object_name()
        self.orbital_data = Orbital(self.object_name,self.tle_file)
        self.orbital_elements = OrbitalElements(self.orbital_data.orbit_elements)
        self.orbital_elements.set_satellite_name(self.object_name)
        self.orbital_elements.set_tle_filename(self.tle_file)


    def get_orbital_elements(self):
        return self.orbital_elements
    
    
    def print_orbital_elements(self):
        print(self.orbital_elements)
    
    
    def set_start_datetime(self,start_datetime):
        self.start_datetime = start_datetime
        
    
    def set_end_datetime(self,end_datetime):
        self.end_datetime = end_datetime
        
    
    def set_motion_descriptor(self,motion_descriptor):
        self.motion_descriptor = motion_descriptor
        
    
    def get_start_datetime(self):
        return self.start_datetime
    
    
    def get_end_datetime(self):
        return self.end_datetime
    
    
    def get_motion_descriptor(self):
        return self.motion_descriptor
    
    
    def get_orbital_data(self):
        return self.orbital_data
    
    
    def get_satellite_name(self):
        return self.object_name
    
    
    def get_tle_filename(self):
        file = os.path.basename(self.tle_file)
        return file
    
    
        
    