def motion_profile(vel, accel, distance, increment):
    tb=distance/vel - 1/accel
    ta=vel/accel

    vels = []
    x = 0.0
    while x < ta:
       vels.append(x*accel)
       x = x + increment
    while x < ta+tb:
       vels.append(vel)
       x = x + increment
    while x <= 2*ta + tb:
       vels.append((x - 2*ta - tb)*-accel)
       x = x + increment

    return vels

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

dist = 20
vel = 3
accel = 1
time = dist/vel - 1/accel + 2*vel/accel
inc = 0.001 #this is like resolution
x = np.arange(0.0,time, inc)
y = motion_profile(vel, accel, dist, inc)

fig, ax = plt.subplots()
ax.plot(x,y)

#plt.xticks(x)

ax.set(xlabel="time(s)", ylabel="vel unit/s", title="triangle motion profile")
ax.grid()

plt.show()
