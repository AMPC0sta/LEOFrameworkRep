#from scipy.integrate import solve_ivp
#using as initial conditions one result of simpleMotionEquations.py
y0 = [1160.639968962924, -2004.4540552412604, 0.0, 2.9536214633011205, -1.4736710551322349, 0.0]

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Gravitational parameter for Earth
mu = 398600  # km^3/s^2

# Define the satellite motion differential equations
def satellite_motion(t, y, mu):
    r = np.sqrt(y[0]**2 + y[1]**2 + y[2]**2)
    ax = -mu * y[0] / r**3
    ay = -mu * y[1] / r**3
    az = -mu * y[2] / r**3
    return [y[3], y[4], y[5], ax, ay, az]

# Initial conditions: [x0, y0, z0, vx0, vy0, vz0]
#y0 = [7000, 0, 0, 0, 7.546, 0]

# Calculate the orbital period
r = 7000  # km
T = 2 * np.pi * np.sqrt(r**3 / mu)  # Orbital period in seconds
print(f"Calculated Orbital Period: {T} seconds")

# Time span for the simulation
t_span = (0, T)  # Simulate for one full orbital period

# Solve the differential equations
sol = solve_ivp(satellite_motion, t_span, y0, args=(mu,), method='RK45')

# Plot the results
plt.plot(sol.y[0], sol.y[1])
plt.xlabel('x [km]')
plt.ylabel('y [km]')
plt.title('Satellite Orbit')
plt.axis('equal')  # Ensure the aspect ratio is equal for x and y
plt.show()
