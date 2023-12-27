import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def eq(x):
    return (x ** 2 + 5 * x * np.sin(x) - 10)


x = fsolve(eq, 15)
t = np.linspace(-20, 20, 100)
plt.plot(t, eq(t))
plt.grid()
print(x)
print(eq((x)))
