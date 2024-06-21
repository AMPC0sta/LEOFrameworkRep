import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import solve_ivp

# Gravitational parameter for Earth
mu = 398600  # km^3/s^2

# Define symbols for sympy
t = sp.symbols('t')
x, y, z, vx, vy, vz = sp.symbols('x y z vx vy vz')

# Define the equations symbolically
r = sp.sqrt(x**2 + y**2 + z**2)
ax = -mu * x / r**3
ay = -mu * y / r**3
az = -mu * z / r**3

# Define the system of equations
eqs = [vx, vy, vz, ax, ay, az]

# Convert the symbolic equations to a numerical function
f = sp.lambdify((t, [x, y, z, vx, vy, vz]), eqs, 'numpy')

# Define the orbital parameters
eccentricity = 0.000328  # Example eccentricity
semi_major_axis = 6786  # Semi-major axis in km (earth_radius + altitude)

# Initial conditions (position and velocity) for an elliptical orbit
# Perigee distance (closest approach)
r_perigee = semi_major_axis * (1 - eccentricity)

# Velocity at perigee
v_perigee = np.sqrt(mu * (1 + eccentricity) / r_perigee)

# Initial conditions: start at perigee
y0 = [r_perigee, 0, 0, 0, v_perigee, 0]

# Calculate the orbital period using the semi-major axis
T_seconds = 2 * np.pi * np.sqrt(semi_major_axis**3 / mu)  # Orbital period in seconds
T_minutes = T_seconds / 60  # Convert orbital period to minutes
print(f"Calculated Orbital Period: {T_minutes} minutes")

# Time span for the simulation: let's run it for one period to observe the motion
t_span = (0, T_seconds)  # Time span in seconds

# Increase resolution by specifying more time points
num_points = 1000  # Increase this number for higher resolution
t_eval = np.linspace(t_span[0], t_span[1], num_points)

# Define the function to pass to solve_ivp
def satellite_motion(t, y):
    return f(t, y)

# Solve the differential equations with higher resolution and tighter tolerances
sol = solve_ivp(satellite_motion, t_span, y0, method='RK45', t_eval=t_eval, rtol=1e-9, atol=1e-12)

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
plt.plot(sol.t / 60, r)
plt.xlabel('Time [minutes]')
plt.ylabel('Distance from Origin [km]')
plt.title('Satellite Distance Over Time')
plt.grid(True)
plt.show()
