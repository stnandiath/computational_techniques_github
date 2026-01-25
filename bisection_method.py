import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*np.cos(x) - x
x = np.linspace(0, 7, 400)
y = f(x)

plt.figure()
plt.plot(x, y)
plt.axhline(0)      
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = 2 cos(x) - x")
plt.grid(True)
plt.show()