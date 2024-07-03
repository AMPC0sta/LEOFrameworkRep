from abc import ABCMeta

from propagatorSuperClass import PropagatorSuperClass

  
class PluginSimpleMotion(PropagatorSuperClass):
     
    def __init__(self):
        super()
        self.plugin_name = 'SimpleMotion'  
        

    def name_to_register_plugin(self):
    
        return self.plugin_name
    

    def set_startime(self,startime):
        pass
    
    def test():
        pass
    
    