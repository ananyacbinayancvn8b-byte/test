import matplotlib.pyplot as plt
import numpy as np 

xpoints=np.array([10,20,70,200])
ypoints=np.array([20,30,150,300])

plt.pilot(xpoints,ypoints,marker='0')


plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("simple line plot")

plt.grid()

plt.show()
