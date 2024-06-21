import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import solve_ivp

# Gravitational parameter for Earth
mu = 398600  # km^3/s^2

# Define symbols for sympy
t = sp.symbols('t')
y = sp.Function('y')(t)
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

# Initial conditions from simpleMotionEquations.py
y0 = [1160.639968962924, -2004.4540552412604, 0.0, 2.9536214633011205, -1.4736710551322349, 0.0]

# Calculate the semi-major axis
earth_radius = 6378  # km
altitude = 408  # km
a = earth_radius + altitude  # semi-major axis in km

# Calculate the orbital period using the semi-major axis
T_seconds = 2 * np.pi * np.sqrt(a**3 / mu)  # Orbital period in seconds
T_minutes = T_seconds / 60  # Convert orbital period to minutes
print(f"Calculated Orbital Period: {T_minutes} minutes")

# Time span for the simulation: let's run it for one and a half periods to observe the motion
t_span = (0, 1 * T_seconds)  # Time span in seconds

# Increase resolution by specifying more time points
num_points = 5630  # Increase this number for higher resolution
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
