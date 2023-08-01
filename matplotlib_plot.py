from matplotlib import pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

plt.plot(x,y)
#plt.bar(x,y)
#plt.scatter(x,y)
#plt.hist(x,y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Ploting Graph")
plt.show()