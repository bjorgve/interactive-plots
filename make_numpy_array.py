import numpy as np


def gaussian(beta, x):
    alpha = (beta/np.pi)**0.5
    return alpha*np.exp(-beta*x**2)


x = np.arange(-np.pi, np.pi, 0.01)
y = np.ones([5, x.size], dtype=float)
# print(x)
for exponent, row in enumerate(y, start=1):
    row[:] = gaussian(10**exponent, x)

np.save('y_file.npy', y)
np.save('x_file.npy', x)
