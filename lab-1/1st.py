# Array multiplication
import numpy as np

A=[[1,2,3],[4,5,6]]
A = np.matrix(A)

B=[[-1,0],[1,3],[2,4]]
B=np.matrix(B)

AB = np.dot(A,B)

print(AB)