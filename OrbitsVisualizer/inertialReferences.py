
import numpy as np

class IntertialReferences:

        def __init__(self):
            pass
        
            
        def rotX(theta_rad):
            
            rotational_X_matrix = np.array(
                                            [
                                                [1,     0,                 0                    ],
                                                [0,     np.cos(theta_rad),  -np.sin(theta_rad)  ],
                                                [0,     np.sin(theta_rad),  np.cos(theta_rad)   ]
                                            ]    
                                          )
            return rotational_X_matrix