import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.972e24     # Mass of Earth, kg

# Orbital parameters
a = 7000e3      # Semi-major axis, meters
e = 0.9         # Eccentricity (example value)
mu = G * M      # Standard gravitational parameter

# Initial position and velocity for an elliptical orbit
# Assuming the initial position is at the perigee (closest point)
x = a * (1 - e)
y = 0
z = 0

# The velocity at perigee for an elliptical orbit
vx = 0
vy = np.sqrt(mu * (1 + e) / (a * (1 - e)))  # Tangential velocity at perigee
vz = 0

# Time parameters
dt = 1  # Time step in seconds
num_steps = 10000  # Number of steps for simulation

# Lists to store trajectory
x_vals, y_vals, z_vals = [x], [y], [z]

# Numerical integration using the Velocity Verlet method
for _ in range(num_steps):
    r = np.sqrt(x**2 + y**2 + z**2)
    ax = -mu * x / r**3
    ay = -mu * y / r**3
    az = -mu * z / r**3
    
    print(x,y,z,vx,vy,vz)
    
    # Update positions
    x += vx * dt + 0.5 * ax * dt**2
    y += vy * dt + 0.5 * ay * dt**2
    z += vz * dt + 0.5 * az * dt**2
    
    # Calculate new accelerations
    r_new = np.sqrt(x**2 + y**2 + z**2)
    ax_new = -mu * x / r_new**3
    ay_new = -mu * y / r_new**3
    az_new = -mu * z / r_new**3
    
    # Update velocities
    vx += 0.5 * (ax + ax_new) * dt
    vy += 0.5 * (ay + ay_new) * dt
    vz += 0.5 * (az + az_new) * dt
    
    # Store positions
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

# Plotting the orbit
plt.plot(x_vals, y_vals)
plt.xlabel('x (meters)')
plt.ylabel('y (meters)')
plt.title('Orbital Trajectory')
plt.axis('equal')
plt.show()
