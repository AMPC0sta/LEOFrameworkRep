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

# Initial conditions from simpleMotionEquations.py
y0 = [1160.639968962924, -2004.4540552412604, 0.0, 2.9536214633011205, -1.4736710551322349, 0.0]

# Calculate the semi-major axis
r0 = np.sqrt(y0[0]**2 + y0[1]**2 + y0[2]**2)
v0 = np.sqrt(y0[3]**2 + y0[4]**2 + y0[5]**2)
energy = 0.5 * v0**2 - mu / r0
a = -mu / (2 * energy)  # Semi-major axis

# For a satellite in LEO with a typical altitude of 700 km above Earth's surface
earth_radius = 6378  # km
altitude = 408  # km
a = earth_radius + altitude  # semi-major axis in km

# Calculate the orbital period using the semi-major axis
T_seconds = 2 * np.pi * np.sqrt(a**3 / mu)  # Orbital period in seconds
T_minutes = T_seconds / 60  # Convert orbital period to minutes
print(f"Calculated Orbital Period: {T_minutes} minutes")

# Time span for the simulation: let's run it for one and a half periods to observe the motion
t_span = (0, 1 * T_seconds)  # Time span in seconds
print (t_span[0])
print (t_span[1])
# Increase resolution by specifying more time points
num_points = 5630  # Increase this number for higher resolution
t_eval = np.linspace(t_span[0], t_span[1], num_points)

# Solve the differential equations with higher resolution and tighter tolerances
sol = solve_ivp(satellite_motion, t_span, y0, args=(mu,), method='RK45', t_eval=t_eval, rtol=1e-9, atol=1e-12)

# Plot the results
plt.plot(sol.y[0], sol.y[1])
plt.xlabel('x [km]')
plt.ylabel('y [km]')
plt.title('Satellite Orbit')
plt.axis('equal')  # Ensure the aspect ratio is equal for x and y
plt.grid(True)
plt.show()

# Plot time series of the satellite's distance from the origin
r = np.sqrt(sol.y[0]**2 + sol.y[1]**2 + sol.y[2]**2)
print(sol)
plt.plot(sol.t / 60, r)
plt.xlabel('Time [minutes]')
plt.ylabel('Distance from Origin [km]')
plt.title('Satellite Distance Over Time')
plt.grid(True)
plt.show()
