import numpy as np
from numpy.linalg import solve

A = np.array([[-4.3, 7.1], [-0.2, 5.6]])

print(A)

b = np.dot(A, np.array([2.0, -5.0]))
print(b)

x = solve(A, b)
print(x)