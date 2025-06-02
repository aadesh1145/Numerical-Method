# Creation of matrix
import numpy as np

A=[]

for i in range(3):
    row=[]
    for j in range(4):
        row.append(float(input(f"Enter the element a{i}{j}:")))
    A.append(row)
A = np.matrix(A)
print(A)