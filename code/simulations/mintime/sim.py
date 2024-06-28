from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_points = 150

mat_file = loadmat('t.mat')
t_values = mat_file['t']
t_list = t_values.tolist()
t_array = np.array(t_list[0])

mat_file_p1 = loadmat('p1.mat')
p1_values = mat_file_p1['p1']
p1_list = p1_values.tolist()

x_data_p1 = np.array(p1_list[0])
y_data_p1 = np.array(p1_list[1])

mat_file_p2 = loadmat('p2.mat')
p2_values = mat_file_p2['p2']
p2_list = p2_values.tolist()

x_data_p2 = np.array(p2_list[0])
y_data_p2 = np.array(p2_list[1])

def get_bounds(p1, p2):
    val = np.concatenate((p1, p2), axis=1)
    xLow = np.min(val[0]) - 0.5
    xUpp = np.max(val[0]) + 0.5
    yLow = np.min(val[1]) - 0.5
    yUpp = np.max(val[1]) + 0.5
    return xLow, xUpp, yLow, yUpp

xLow, xUpp, yLow, yUpp = get_bounds(p1_list, p2_list)

fig, ax = plt.subplots()
ax.set_xlim(xLow, xUpp)
ax.set_ylim(yLow, yUpp)

cart_width = 0.4
cart_height = 0.2
pole_length = 1.5

cart = plt.Rectangle((0, 0), cart_width, cart_height, fc='b')
pendulum, = ax.plot([], [], marker='o', color='r', markersize=10) 

ax.add_patch(cart)

def update(frame):
    if frame < num_points:
        cart.set_xy([x_data_p1[frame] - cart_width/2, y_data_p1[frame] - cart_height/2])
        pendulum.set_data([x_data_p1[frame], x_data_p2[frame]], [y_data_p1[frame], y_data_p2[frame]])
    return cart, pendulum

ani = FuncAnimation(fig, update, frames=num_points+1, blit=True, interval=50)  

plt.show()
