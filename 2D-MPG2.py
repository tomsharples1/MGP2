import math
import numpy as np
import matplotlib.pyplot as plt

F_m = 230 / 2.6
v0 = 2.6
u = 0.64
m = 200

def X(t, b, k, theta):
    theta = np.radians(theta)
    return F_m / (2 * m) * (np.cos(theta) - u * np.sin(theta)) * (t ** 2) + v0 * np.cos(theta) * t

def X1(t, b, k, theta):
    theta = np.radians(theta)
    return F_m/m * (math.cos(theta) - u*math.sin(theta))*t

def Y(t, b, k, theta):
    theta = np.radians(theta)
    return (F_m / k) * np.sin(theta) * (1 - np.exp((-k / b) * t))

time = np.arange(0, 20, 0.05)


b_values = [200, 300, 400]
k_values = [300, 400]
theta_values = [10, 20, 30]


plt.figure(figsize=(10, 6))
for theta in theta_values:
    x_values = X(time, 300, 300, theta)
    label = f'theta={theta}'
    plt.plot(time, x_values, label=label)
        

plt.title("Collision with the wall at angle, x direction")
plt.xlabel("Time")
plt.ylabel("X(t)")
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
for b in b_values:
    for k in k_values:
        if b**2 < 800*k:
            for theta in theta_values:
                y_values = Y(time, b, k, theta)
                label = f'b={b}, k={k}, theta={theta}'
                plt.plot(time, y_values, label=label)
        

plt.title("Collision with the wall at angle, y direction")
plt.xlabel("Time")
plt.ylabel("Y(t)")
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
for b in b_values:
    for k in k_values:
        if b**2 < 800*k:
            for theta in theta_values:
                x_values = X(time, b, k, theta)
                y_values = Y(time, b, k, theta)
                label = f'b={b}, k={k}, theta={theta}'
                plt.plot(x_values, y_values, label=label)
        

plt.title("Collision with wall at angle, X against Y")
plt.xlabel("X position")
plt.ylabel("Y position")
plt.legend()
plt.show()
