import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Input for rearranged function g(x)
gx = input("Enter the rearranged equation g(x) in python syntax: ")

# Define g(x)
def G(x, gx):
    return eval(gx)

def g(x):
    return G(x, gx)

# Input initial approximation
a = float(input("Enter your initial approximation: "))

# Input tolerable error and max iterations
e = float(input("Enter tolerable error: "))
n = int(input("Enter the maximum number of iterations: "))

itr = 1
lst = []
a_list = [a]

while itr <= n:
    b = g(a)
    err = abs(b - a)
    lst.append([itr, a, b, err])
    a_list.append(b)

    if err < e:
        lst = pd.DataFrame(lst, columns=['Iteration', 'X_n', 'X_n+1', 'Error']).to_string(index=False)
        print(lst)
        print(f"Approximate root is {b} in {itr} iteration.")
        break

    a = b
    itr += 1

if itr > n:
    print(f"Solution doesn't converge in {n} iterations.")

# Plotting
x = np.linspace(-5, 5, 1000)
plt.plot(x, g(x), label='g(x)', color='orange')
plt.plot(x, x, label='y = x', linestyle='--', color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Fixed Point Iteration")
plt.legend()
plt.scatter(a_list, [g(val) for val in a_list], color='red')

for i, val in enumerate(a_list):
    plt.text(val, g(val), f'{i+1}')

plt.show()
