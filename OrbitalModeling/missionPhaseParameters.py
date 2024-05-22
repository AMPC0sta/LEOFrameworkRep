from pyorbital.orbital import Orbital

class MissionPhaseParameters:
    
    def __init__(self,phase_name,tle_file = None):
        self.phase_name = phase_name
        self.tle_file = tle_file
        
    
    def read_object_name(self):
        if self.tle_file != None:
            f = open(self.tle_file,'r')
            self.object_name = f.readline()
            f.close()
        else:
            raise RuntimeError("There's no TLE file for this mission phase!")


    def load_TLE_data(self):
        self.orbital_data = Orbital(self.object_name,self.tle_file)
