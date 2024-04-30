from pyorbital import tlefile as tle_list

class CelestrakObjects:
    
    def __init__(self):
        self.satellites_list = []
        for node in tle_list.SATELLITES:
            self.satellites_list.append(node)