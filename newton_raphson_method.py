#Consider the function f(x) = 2 cos x − x. Consider the three initial guesses x0 = 0.5, π & 2π and for these guesses find the roots using Newton-Raphson method.import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*np.cos(x) - x

def df(x):
    return -2*np.sin(x) - 1

x = np.array([0.5, np.pi, 2*np.pi]) #Guesses
tolerance = 1e-6
max = 100

for i in range(max):
    y = f(x)
    slope = df(x)

    step = y / slope
    x = x - step
    
    if np.all(abs(step) < tolerance):
        print(f"Converged at iteration {i+1}")
        break

print(f"Final Root: {x}")