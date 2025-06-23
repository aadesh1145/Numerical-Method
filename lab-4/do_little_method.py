import numpy as np
from scipy.linalg import lu, lu_solve,lu_factor

n = int(input('Enter the number of variables:'))
A=[]
B=[]

for i in range(n):
    A.append(list(map(float,input(f'Enter {i+1} row in given matrix:').split())))
    

for i in range(n):
    B.append(list(map(float,input(f'Enter {i+1} row in given matrix:').split())))
    

P,L,U =lu(A)
lum = lu_factor(A)

print(f'Lower trianglular matrix:\n {L}')
print(f'Upper triangular matrix :\n{U}')
print(f'Permutation matrix is :\n {P}')

x= lu_solve(lum,B)
print(f'Solution : {np.round(x,6)}')

