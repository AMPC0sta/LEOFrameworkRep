
class VisualizerParameters:
    
    # Constructor
    def __init__(self,e_radius):
        if e_radius == None:
           self.e_radius = 6371 # Default Earth radius in km's
        else:
            self.e_radius = e_radius
            