import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import sys //Could be used if sys.exit() was used

# Hard coded function 
# def f(x):
#     # return np.exp(x)-np.sin(x)-9

eqn = input("Enter the equationin x using python syntax:")

def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)
while True:
   a = float(input("Enter your 1st approximation: "))
   b = float(input("Enter your 2nd approximation: "))

   if f(a)*f(b)>0:
        print(f"No root lies between the interval of {a},{b} \n Please enter new approximation \n")

   elif f(a)==f(b):
        print("The solution tends to infininty as both function will be equal \n Please enter new approximation \n")

   else:
        break

e = float(input("Enter tolerable error: "))
n = int(input("Enter the maximum number of iterations: "))
itr = 1
lst = []
mid = []

while(itr<=n):

    c = (a+b)/2
        
    err = abs(b-a)
    lst.append([itr,a,b,c,f(a),f(b),f(c),err])
    mid.append(c)
    
    if f(a)*f(c)<0:
        b = c
        
    else:
        a = c

    if err<e:
        lst=pd.DataFrame(lst,columns=['Iteration','a','b','c','f(a)','f(b)','f(c)','Error']).to_string(index=False)
        print(lst)

        print(f"Approximate root is {c} in {itr} iterations.")
        break
    itr +=1

if itr>n:
    print(f"Solution doesn't converge is {n} iterations.")

x = np.linspace(-5,5,1000)
plt.plot(x,f(x),color='r',label="transendental curve")
plt.axhline(0,0,color='g')
plt.axvline(0,0,color='g')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Bisection Method")
plt.legend()
plt.scatter(mid, [f(c) for c in mid])

for i,val in enumerate(mid):
    plt.text(val,f(val),f'{i+1}')

plt.show()


# Code given by sir
# a = float(input("Enter your 1st approximation: "))
# b = float(input("Enter your 2nd approximation: "))

# if f(a)*f(b)>0:
#     print(f"No root lies between the interval of {a},{b}")
#     sys.exit()

# else:
#     e = float(input("Enter tolerable error: "))
#     n = int(input("Enter the maximum number of iterations: "))
#     itr = 1
#     lst = []
#     mid = []

#     while(itr<=n):

#         c = (a+b)/2

#         if f(a)*f(c)<0:
#             b = c
        
#         else:
#             a = c
        
#         err = abs(b-a)
#         lst.append([itr,a,b,c,f(a),f(b),f(c),err])
#         mid.append(c)

#         if err<e:
#             lst=pd.DataFrame(lst,columns=['Iteration','a','b','c','f(a)','f(b)','f(c)','Error']).to_string(index=False)
#             print(lst)

#             print(f"Approximate root is {c} in {itr} iterations.")
#             break
#         itr +=1

#     if itr>n:
#         print(f"Solution doesn't converge is {n} iterations.")

# x = np.linspace(-5,5,1000)
# plt.plot(x,f(x),color='r',label="transendental curve")
# plt.axhline(0,0,color='g')
# plt.axvline(0,0,color='g')
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("Bisection Method")
# plt.legend()
# # plt.scatter(mid,f(mid)) //doesn't work for lists if equation is user defined
# plt.scatter(mid, [f(c) for c in mid])

# for i,val in enumerate(mid):
#     plt.text(val,f(val),f'{i+1}')

# plt.show()