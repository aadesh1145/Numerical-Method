#To find the dominant eigen value and the corresponding eigen vector of matrix using power method.

import numpy as np
from pandas import DataFrame 

n = int(input('Enter the order of matrix: '))
A = []

for i in range(n):
    A.append(list(map(float,input(f'Enter {i+1} row:').split())))

A = np.array(A)
print('The matrix is A: \n',np.matrix(A))

x = np.array(list(map(float,input('Enter the initial vector:').split())))
x = np.array(x)

print('The initial vector is: \n',np.matrix(x))

e = float(input('Enter tolerable error: '))
N = int(input('Enter the max number of iterations: '))
itr = 1
old_eigen = 0
lst = []

while itr<=N:
    y = np.dot(A,x)
    max_eigen = abs(max(y,key=abs))

    for i in range(n):
        x = y/max_eigen
    
    lst.append([itr,max_eigen]+[x[i] for i in range(n)])
    error = abs(max_eigen-old_eigen)

    if (error<e):
        break
    
    old_eigen = max_eigen
    itr+=1

if (itr>N):
    print(f'Method doesnot converge in {itr} iteration.')
else:
    lst = DataFrame(lst,columns=['iteration','Max Eigen Value']+[f'x{i+1}' for i in range(n)]).to_string(index=False)
    print(lst)
    print(f'The dominant eigen value is {max_eigen} in {itr} iteration')
    print('Corresponding eigen vector is: \n',x)




    
