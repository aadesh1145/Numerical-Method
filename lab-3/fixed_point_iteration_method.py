import numpy as np
import sys 
import pandas as pd
import matplotlib.pyplot as plt

# eqn=input("Enter the equation in x using python syntax: ")

# def F(x,eqn):
#     return eval(eqn)

def f(x):
    return np.sqrt(4*x + 10) 

a = float(input("Enter your approximation: "))
e= float(input("Enter the tolerable error: "))
n=int(input("Enter the maximum number of iterations: "))
itr = 1

while itr<=n:

    x = f(a)
    err = abs(a-x)

    if err<e:
        print(f"Approximate root is {x} in {itr} iterations.")
        break
    
    a = x
    itr+=1

if itr>n:
    print(f"Solution doesn't converge in {n} iterations.")





