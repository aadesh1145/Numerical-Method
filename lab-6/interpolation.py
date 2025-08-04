#interpolation
#to interpolate the given value using Lagrange interpolation
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))
X = np.array(list(map(float, input("Enter all x's: ").split())))
y = np.array(list(map(float, input("Enter all y's: ").split())))

print("The data points are: ")
for i in range(n):
    print(X[i], y[i])

x = sp.symbols('x')

s = 0
x_p = float(input('Enter the point to interpolate:'))
for i in range(n):
    lf = 1
    for j in range(n):
        if i != j:
            lf *= (x - X[j]) / (X[i] - X[j])
    s += y[i] * lf

poly = sp.simplify(s)
print(poly)
val = poly.subs(x, x_p)
print(f"The interpolated value at {x} is {val}")

f = sp.lambdify(x, poly, 'numpy')
w = np.linspace(-10, 10, 1000)
plt.plot(w, f(w), color='black')
plt.scatter(x_p, val)
plt.grid(True)
plt.show()