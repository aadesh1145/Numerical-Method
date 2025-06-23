#to solve the system of linear equation by Guass Elimination with partial pivoting using python programming

import numpy as np

n = int(input('Enter the number of variables: '))
A = []

for i in range(n):
    A.append(list(map(float,input(f'Enter {i+1} row in given matrix:').split())))

A = np.array(A)
print("The augmented matrix A is:")
print(np.matrix(A))

for i in range (n):
    max_row = np.argmax(np.abs(A[i:,i]))+i
    A[[i,max_row]] = A[[max_row,i]]

    for j in range(i+1,n):
        A[j] = A[j] - A[i]*(A[j,i])/A[i,i]

print('The upper triangular matrix is : ')
print(np.matrix(A))

x = np.zeros(n)

for i in range(n-1,-1,-1):
    x[i] = (A[i,-1]-np.sum(A[i,i+1:n]*x[i+1:n]))/A[i,i]

print('\n The solution is : ')
for i in range(n):
    print(f'x{i+1}={round(x[i],6)}')