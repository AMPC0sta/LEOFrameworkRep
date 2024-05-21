

class Mission:
    
    def __init__(self,mission_name,phases=None):
        
        self.mission_name = mission_name
        if phases != None:
            self.phases = phases
            
        