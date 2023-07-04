import matplotlib.pyplot as plt
import numpy as np
'''
xpoints = np.array([1,4,8,10])
ypoints = np.array([10,64,25,90])

plt.plot(xpoints, ypoints,ls = ':', marker = 'o', ms = 15, mec = 'r', mfc = 'r')
plt.show()
'''
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(color = 'green', ls = '--', linewidth = 0.5)
plt.show()