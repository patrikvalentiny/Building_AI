import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])


def sigmoid(z):
    z = (z @ x)
    return 1 / (1 + math.exp(-z))


# calculate the output of the sigmoid for x with all three coefficients
print(sigmoid(c1))
print(sigmoid(c2))
print(sigmoid(c3))

