import numpy as np
import matplotlib.pyplot as plt

def gaussElim(A, b):
    n = len(b)
    # Elimination phase
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0.0:
                # if not null define λ
                lam = A[i, k] / A[k, k]
                # we calculate the new row of the matrix
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                # we update vector b
                b[i] = b[i] - lam * b[k]
    # backward substitution
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(A[k, k+1:n], b[k+1:n])) / A[k, k]
    
    return b

if __name__ == "__main__":

    # Define the points
    x = np.array([-0.1, -0.02, 0.02, 0.1])
    y = np.cos(x)

    # Set up the linear system
    A = np.zeros((4, 4))
    b = np.zeros(4)

    for i in range(4):
        A[i] = [x[i]**3, x[i]**2, x[i], 1]
        b[i] = y[i]

    # Solve the linear system
    coefficients = gaussElim(A, b)

    # Define the polynomial function
    def p(x):
        return coefficients[0]*x**3 + coefficients[1]*x**2 + coefficients[2]*x + coefficients[3]

    # Plot the polynomial and f(x) using matplotlib
    x_vals = np.linspace(-0.1, 0.1, 100)
    plt.plot(x_vals, p(x_vals), label='p(x)')
    plt.plot(x, y, 'ro', label='f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()