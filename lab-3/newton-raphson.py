import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

eqn = input("Enter the equation in x using python syntax:")

def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)

def g(f,x,h=1e-10):
    return (f(x+h)-f(x-h))/(2*h)

while True:
    a = float(input("Enter your approximation: "))
    
    if g(f,a)==0:
        print("Division by 0, Change initial approximation\n")
    
    else:
        break

e = float(input("Enter tolerable error: "))
n=int(input("Enter the maximum number of iterations: "))
itr = 1
lst =[]
b_list=[]

while(itr<=n):

    if g(f,a)==0:
        print("Division by 0 occurred, program exited")
        sys.exit()
    
    b = a-(f(a)/g(f,a))

    err= abs(f(b))
    lst.append([itr,a,b,err])
    b_list.append(b)

    if err<e:
        lst = pd.DataFrame(lst,columns=['Iteration','X_n','X_n+1','Error']).to_string(index=False)
        print(lst)

        print(f"Approximate root is {b} in {itr} iteration.")
        break
    
    a = b
    itr+=1

if itr>n:
    print(f"Solultion doesn't converge in {n} iterations.")

x = np.linspace(-5,5,1000)
plt.plot(x,f(x),color='r',label=eqn)
plt.axhline(0,0,color='g')
plt.axvline(0,0,color='g')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Newton Raphson Method")
plt.legend()
plt.scatter(b_list, [f(b) for b in b_list])

for i,val in enumerate(b_list):
    plt.text(val,f(val),f'{i+1}')

plt.show()
