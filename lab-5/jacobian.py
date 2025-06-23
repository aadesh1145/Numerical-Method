#To solve system of linear equation by Jacobi iteration ,
# order = 3 A= [8 3 2 13] [1 5 1 7] [2 1 6 9] intial root = [0 0 0] error = 1e-10

import numpy as np
import sys
from pandas import DataFrame 

n = int(input('Enter the order of matrix: '))
A = []
print('Enter augmented matrix with A_ii != 0: ')

for i in range(n):
    A.append(list(map(float,input(f'Enter {i+1} row:').split())))

A = np.array(A)

print('The augmented matrix [A] is:\n',np.matrix(A))

x = np.array(list(map(float,input('Enter intial roots: ').split())))
x=np.array(x)
print('Initial values : \n',np.matrix(x))

e = float(input('Enter tolerable error: '))
N = int(input('Enter the max number of iterations: '))
itr = 1
lst = []
while itr<=N:
    x_old = np.copy(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i,j]*x_old[j]
            
        x[i] = (A[i,-1]-s)/A[i,i]

    err = np.abs(x-x_old)
    lst.append([itr] + [x[i] for i in range(n)])
    if np.all(err<e):
        break 
    itr += 1

if (itr>N):
    print(f'Solution doesnot converge in {itr} iteration')

else:
    lst = DataFrame(lst,columns=['iteration']+[f'x{i+1}' for i in range(n)]).to_string(index=False)
    print(lst)
    print(f'The solution in {itr} iteration is: \n')
    for i in range(n):
        print(f'x{i+1}={x[i]}')
    
