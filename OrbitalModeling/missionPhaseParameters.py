from pyorbital.orbital import Orbital

class MissionPhaseParameters:
    
    def __init__(self,phase_name,tle_file = None):
        self.phase_name = phase_name
        self.tle_file = tle_file
        
    
    def read_object_name(self):
        if self.tle_file != None:
            
            
            # If TLE (Two Lines Element file has 3 lines (than consider first line as being satellite name), other wise satellite name is the filename)
            line = []
            with open(self.tle_file,'r') as f:
                for count,line[count] in enumerate(f):
                    pass
            if count + 1 == 3:
                self.object_name = count[0]
            else:
                self.object_name = self.tle_file.split('\n')[len(self.tle_file.split)]
            f.close()
        else:
            raise RuntimeError("There's no TLE file set, for this mission phase!")


    def load_TLE_data(self):
        self.orbital_data = Orbital(self.object_name,self.tle_file)


    def get_orbital_elements(self):
        return self.orbital_data.orbit_elements
    
    