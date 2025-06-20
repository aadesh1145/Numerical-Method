# To solve the system of linear equation by using Guass Jordan Method
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
    A[i]=A[i]/A[i,i]

    for j in range(n):
        if j!=i:
            A[j] = A[j] - A[i]*(A[j,i])

print('The upper triangular matrix is : ')
print(np.matrix(A))

print("The normal matrix is :")
print(np.matrix(A))
x=A[:,-1]

print('\n The solution is : ')
for i in range(n):
    print(f'x{i+1}={round(x[i],6)}')