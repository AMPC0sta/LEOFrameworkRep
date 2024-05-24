from pyorbital.orbital import Orbital
from datetime import datetime, timezone

import sys
import os

# Move backwards on directory tree to allow to import custom modules from others folders
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Common.mathUtils import MathUtils
from Common.orbitalMechanics import *

class OrbitalElements:
    
    def __init__(self,orbital_elements):
        self.orbital_elements = orbital_elements
        
        
        
    def __str__(self):
        oe = self.orbital_elements
        utc_time = datetime.now()
        mean_motion=oe.mean_motion
        return (
            f"Time (UTC): {utc_time.isoformat()}\n"
            f"Mean Anomaly: {oe.mean_anomaly} rads\n"
            f"Mean Motion: {mean_motion} revolutions per day\n"
            f"Semi Major Axis: {oe.semi_major_axis} km\n"
            f"Argument of Perigee: {oe.arg_perigee} rads\n"
            f"Eccentricity: {oe.excentricity}\n"
            f"Inclination: {oe.inclination} rads\n"
            f"RAAN (Right Ascension of Ascending Node): {oe.right_ascension} rads\n"
            f"Period {oe.period} minutes\n"
        )
        
        
    def to_show_on_widget(self):
        oe = self.orbital_elements
        utc_time = datetime.now()
        mean_motion=oe.mean_motion
        
        elements = [
            ("Time (UTC)", utc_time.isoformat()),
            ("Mean Anomaly (degrees)", MathUtils.rad2deg(oe.mean_anomaly)),
            ("Mean Motion (revolutions/day)", mean_motion),
            ("Semi Major Axis (km)", OrbitalMechanics.earth_radius * oe.semi_major_axis),
            ("Argument of Perigee (degrees)", MathUtils.rad2deg(oe.arg_perigee)),
            ("Eccentricity", oe.excentricity),
            ("Inclination (degrees)", MathUtils.rad2deg(oe.inclination)),
            ("RAAN (Right Ascension of Ascending Node) (degrees)", MathUtils.rad2deg(oe.right_ascension)),
            ("Period (minutes)",oe.period)
        ]
        
        return elements