#to evaluate integral using simpson-3/8 method
import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: '))
n = int(input('Enter the no. of sub-intervals: '))
h = (b-a)/n

if n % 3 != 0:
    raise ValueError("Number of sub-intervals must be a multiple of 3 for Simpson's 3/8 Rule.")

func = input('Enter the integrand function in python syntax: ')
def F(x, func):
    return eval(func)

def y(x):
    return F(x, func)

x = np.linspace(a, b, n+1)
y_points = [y(x) for x in x]

integral = 0
S1 = 0
S2 = 0

for i in range(1, n):
    if i % 3 == 0:
        S2 += y(x[i])
    else:
        S1 += y(x[i])


integral = 3*h/8 * (y(x[0]) + 3 * S1 + 2 * S2 + y(x[n]))

print(f"The approximate integral value is {integral}")

plt.axhline(y=0, color='green', linewidth=1)
plt.axvline(x=0, color='green', linewidth=1)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Simpson's 3/8 Rule Approximation")
plt.tight_layout()
plt.plot(x, y_points)
x_val = np.linspace(-10, 10, 1000)
plt.plot(x_val, [y(x) for x in x_val])


for i in range(0, n, 3):
    x_s = x[i:i+4]
    y_s = y_points[i:i+4]

    plt.fill_between(x_s, y_s)

plt.grid(True)
plt.show()