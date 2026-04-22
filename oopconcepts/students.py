import matplotlib.pyplot as plt
import numpy as np

students=["Arun","alice","Akhil","Bob"]
marks=[56,89,43,99] 
plt.plot(students,marks,marker='o')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")


plt.grid()
plt.show()