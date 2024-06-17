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

# Calculate specific angular momentum
h_vec = np.cross(y0[:3], y0[3:])
h = np.linalg.norm(h_vec)

# Calculate eccentricity vector
e_vec = (np.cross(y0[3:], h_vec) / mu) - (y0[:3] / r0)
e = np.linalg.norm(e_vec)  # Eccentricity

# Calculate the orbital period using the semi-major axis
T = 2 * np.pi * np.sqrt(a**3 / mu)  # Orbital period in seconds
print(f"Calculated Orbital Period: {T} seconds")
print(f"Calculated Eccentricity: {e}")

# Time span for the simulation: let's run it for one and a half periods to observe the motion
t_span = (0, 1.5 * T)

# Solve the differential equations
sol = solve_ivp(satellite_motion, t_span, y0, args=(mu,), method='RK45', rtol=1e-9, atol=1e-12)

# Plot the results
plt.plot(sol.y[0], sol.y[1])
plt.xlabel('x [km]')
plt.ylabel('y [km]')
plt.title('Satellite Orbit')
plt.axis('equal')  # Ensure the aspect ratio is equal for x and y
plt.grid(True)
plt.show()
