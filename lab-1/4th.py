# Plotting in graph
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,1000)#linspace choose 50 points in the given range
# print(x) 

def y(x):
    return x**2

plt.plot(x,y(x),label='parabola',color='red')
plt.scatter(x,y(x))
plt.axhline(0,0,color='blue')
plt.axvline(0,0,color='green')
plt.xlabel('x value')
plt.ylabel('y value')
plt.grid(True)
plt.legend()
plt.title('Graph of parabola')
plt.show()



