import math
import numpy as np
import matplotlib.pyplot as plt

#Define the function
def f(x):
    return 2*np.cos(x) - x
x = np.linspace(0, 7, 400)
y = f(x)

# Defining the error tolerance , the maximum number of iterations and the interval
eps = 1e-3
Nmax = 100
a = 0.0
b = 7.0

# This function finds a root of the equation f(x)=0 using the bisection method
def Bisection(Xminus, Xplus, Nmax, eps):
    roots = []  

    for it in range(Nmax):
        x = (Xplus + Xminus) / 2.0
        roots.append(x)

        if f(Xplus) * f(x) > 0.0:
            Xplus = x
        else:
            Xminus = x

        if abs(f(x)) < eps:
            print("Converged in", it+1, "iterations")
            break

    return np.array(roots)

roots = Bisection(a, b, Nmax, eps)

plt.figure()
plt.plot(x, y)
plt.axhline(0)      
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = 2 cos(x) - x")
plt.grid(True)
plt.show()