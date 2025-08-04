# To fit the second degree curve y = a+bx+cx**2 to the fix data using least square method.
import numpy as np
import sys
import scipy.linalg as slg
import matplotlib.pyplot as plt
n = int(input("Enter no of data points: "))
sys.stdout.flush()
x = np.array(list(map(float,input('Enter all x-data: ').split())))
y = np.array(list(map(float,input('Enter all y-data: ').split())))

A = [[n,np.sum(x),np.sum(x**2)],
     [np.sum(x),np.sum(x**2),np.sum(x**3)],
     [np.sum(x**2),np.sum(x**3),np.sum(x**4)]]

B = [[np.sum(y)],[np.sum(x*y)],[np.sum(x**2*y)]]

print('The coefficient matrix of normal equation is A:\n',np.matrix(A))
print('The column matrix of the normal equation is B \n',np.matrix(B))

coeff = slg.solve(A,B)
a, b, c = coeff.flatten()

print(f'The curve of best fit is {coeff[0]}+{coeff[1]}x+{coeff[2]}x^2 ')

# Define function for the fitted curve
def f(x):
    return a + b*x + c*x**2

# Generate x values for plotting the smooth curve
x_fit = np.linspace(min(x) - 1, max(y) + 1, 500)
y_fit = f(x_fit)

# Plot the data points and the fitted curve
plt.figure(figsize=(8, 6))
plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve: $y = a + bx + cx^2$')
plt.scatter(x, y, color='blue', label='Data Points')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit of a Second Degree Polynomial')
plt.legend()
plt.show()