import numpy as np
from numpy.linalg import solve

def gaussElim(matrix, vector):
    n = len(vector)
    # Elimination phase
    for k in range(0, n-1):
        for i in range(k+1, n):
            if matrix[i, k] != 0.0:
                # if not null define λ
                lam = matrix[i, k] / matrix[k, k]
                # we calculate the new row of the matrix
                matrix[i, k+1:n] = matrix[i, k+1:n] - lam * matrix[k, k+1:n]
                # we update vector b
                vector[i] = vector[i] - lam * vector[k]
    # backward substitution
    for k in range(n-1, -1, -1):
        vector[k] = (vector[k] - np.dot(matrix[k, k+1:n], vector[k+1:n])) / matrix[k, k]
    
    return vector

A = np.array([[2.0, 0.0, 1.0], [-1.0, 7.0, 1.0], [5.0, -1.0, 1.0]])
b =  np.dot(A, np.array([-4.0, -50.0, -26.0]))
print(gaussElim(A,b), "is my function")
print("")

C = np.array([[2, 0, 1], [-1, 7, 1], [5, -1, 1]])
d =  np.dot(C, np.array([-4, -50, -26]))

linalg_x = solve(C, d)
print(linalg_x, "is numpy's")
