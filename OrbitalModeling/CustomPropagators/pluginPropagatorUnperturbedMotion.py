from abc import ABCMeta
from propagatorSuperClass import PropagatorSuperClass

class PluginPropagatorUnperturbedMotion(PropagatorSuperClass):
    
    plugin_name = 'UnperturbedPropagator'
    
    def __init__(self,M,e,O,o,i,n,epoch):
        super().__init__(M,e,O,o,i,n,epoch)
        
    
    def name_to_register_plugin():
        global plugin_name
        
        return plugin_name
    