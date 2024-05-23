from pyorbital.orbital import Orbital

class MissionPhaseParameters:
    
    def __init__(self,phase_name,phase_position=0,tle_file = None):
        self.phase_name = phase_name
        self.tle_file = tle_file
        self.phase_position = phase_position
        
    
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
                self.object_name = f.readline()
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
        self.orbital_elements = self.orbital_data.orbit_elements


    def print_orbital_elements(self):
        print(self.orbital_elements.__str__())
    
    