import numpy as np
import matplotlib.pyplot as plt

def simulate_trajectory(v0, angle_deg, mass=0.145, drag_coeff=0.47, area=0.0042, dt=0.001):
    g, rho = 9.81, 1.225
    rad = np.radians(angle_deg)
    vx, vy = v0 * np.cos(rad), v0 * np.sin(rad)
    x, y = 0.0, 0.0
    x_points, y_points = [x], [y]
    
    while y >= 0:
        v = np.hypot(vx, vy)
        f_drag = 0.5 * rho * drag_coeff * area * (v ** 2)
        ax = -(f_drag / mass) * (vx / v)
        ay = -g - (f_drag / mass) * (vy / v)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        if y >= 0:
            x_points.append(x), y_points.append(y)
            
    return x_points, y_points

angles = [30, 45, 60]
for ang in angles:
    x_vals, y_vals = simulate_trajectory(v0=45.0, angle_deg=ang)
    plt.plot(x_vals, y_vals, label=f"{ang} degrees")

plt.title("Projectile Motion with Air Resistance")
plt.legend()
plt.savefig("graph.png") 
plt.show()
