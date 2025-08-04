#to solve dy/dx = f(x, y), y(x0)=y0 using R-K-4 method

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ode = input('Enter the function dy/dx in terms of x and y using Python syntax: ')

def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

x = float(input('Enter initial value of x: '))
y = float(input('Enter initial value of y: '))
b = float(input('Enter last point at which solution is required: '))
n = int(input('Enter the number of steps: '))

h = (b - x) / n
t = []
xval = [x]
yval = [y]

for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x+h/2, y+k1/2)
    k3 = h * f(x+h/2, y+k2/2)
    k4 = h * f(x+h, y+k3)

    y = y + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    x = x + h

    t.append([x, y])
    xval.append(x)
    yval.append(y)

t = pd.DataFrame(t, columns=['x', 'y'])
print(t)


plt.axhline(y=0, color='green', linewidth=1)
plt.axvline(x=0, color='green', linewidth=1)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("R-K-4 method")

plt.plot(xval, yval)
plt.scatter(xval, yval, color='black')
plt.show()
