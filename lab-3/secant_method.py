import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

eqn = input("Enter the equation in x using python syntax:")

def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)

while True:
    a = float(input("Enter your 1st approximation: "))
    b = float(input("Enter your 2nd approximation:"))

    if f(a)==f(b):
        print("Division by 0, Change initial approximations\n")
    
    else:
        break

e = float(input("Enter tolerable error: "))
n = int(input("Enter the maximum number of iterations: "))
itr = 1
lst =[]
c_list=[]

while(itr<=n):

    if f(b)==f(a):
        print("Division by 0 occurred,program exited")
        sys.exit()
    

    c = (a*f(b)-b*f(a))/(f(b)-f(a))

    err = abs(f(c))
    lst.append([itr,a,b,f(a),f(b),c,err])
    c_list.append(c)

    if err<e:
        lst = pd.DataFrame(lst,columns=['Iteration','a','b','f(a)','f(b)','c','Error']).to_string(index=False)   
        print(lst)

        print(f"Aprroximate root is {c} in {itr} iterations.")
        break
    a=b
    b=c
    itr+=1

if itr>n:
    print(f"Solution doesn't converge in {n} iterations.")

x = np.linspace(-5,5,1000)
plt.plot(x,f(x),color='r',label=eqn)
plt.axhline(0,0,color='g')
plt.axvline(0,0,color='g')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Secant Method")
plt.legend()
plt.scatter(c_list, [f(c) for c in c_list])

for i,val in enumerate(c_list):
    plt.text(val,f(val),f'{i+1}')

plt.show()

