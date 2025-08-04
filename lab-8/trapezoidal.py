#to evaluate integral using trapezoidal method
import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: '))
n = int(input('Enter the no. of sub-intervals: '))
h = (b-a)/n

func = input('Enter the integrand function in python syntax: ')
def F(x, func):
    return eval(func)

def y(x):
    return F(x, func)

x = np.linspace(a, b, n+1)
y_points = [y(x) for x in x]

integral = 0
S = 0

for i in range(1, n):
    S += y(x[i])

integral = h/2 * (y(x[0]) + 2 * S + y(x[n]))

print(f"The approximate integral value is {integral}")

plt.axhline(y=0, color='green', linewidth=1)
plt.axvline(x=0, color='green', linewidth=1)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Trapezoidal Approximation ")
plt.tight_layout()
plt.plot(x, y_points)
x_val = np.linspace(-10, 10, 1000)
plt.plot(x_val, [y(x) for x in x_val])


for i in range(n):
    x_s = [x[i], x[i], x[i+1], x[i+1]]
    y_s = [0, y_points[i], y_points[i+1], 0]

    plt.fill(x_s, y_s, color='red', edgecolor='green', alpha=0.2)

plt.grid(True)
plt.show()