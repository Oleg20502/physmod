#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

import numpy as np

t = np.linspace(0,100,1000)

A1 = 1
A2 = 2

y1 = A1*np.sin(t)
y2 = A2*np.sin(2*t) + y1

x1 = A1 * np.cos(t)
x2 = A2 * np.cos(2*t) + x1

plt.close("all")
fh, ah = plt.subplots()

def plot_frame(ah, i):
    ah.plot ([0.0, x1[i], x2[i]], [0.0, y1[i], y2[i]])
    ah.scatter([x1[i]], y1[i], color="red")
    ah.scatter([x2[i]], y2[i], color="green")
    
plot_frame(ah, 10)

#%%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.close("all")
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')
sp1, = plt.plot([], [], 'go')
sp2, = plt.plot([], [], 'bo')

def init():
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-3.0, 3.0)
    return ln,

def update(frame):
    x1, x2, y1, y2 = frame['x1'], frame['x2'], frame['y1'], frame['y2']
    ln.set_data([0.0, x1, x2], [0.0, y1, y2])
    sp1.set_data([x1,x1], [y1,y1])
    sp2.set_data([x2,x2], [y2,y2])
    
    return ln, sp1, sp2,

frames = np.zeros([x1.size], dtype=[('x1',np.float), ('x2',np.float), ('y1',np.float), ('y2',np.float)])

frames['x1'] = x1
frames['x2'] = x2
frames['y1'] = y1
frames['y2'] = y2

ani = FuncAnimation(fig, update, frames=frames,
                    init_func=init, blit=True)

plt.show()
