

def sqrt(x,printhow=0, initial_guess=1,kmax=100,tol=1e-14):
    #computing s = sqrt(x) using Newton's method
    #Input:
    # initial_guess is the initial guess for newton's method, default is 1
    #kmax is the max number of iterations, default is 100
    # tol is the tolerance to terminate newton's method, default is 1e-14
    if x < 0:
        return -1
    
    if x == 0:
        return 0
    #transfer x from int to float
    x = x*1.0

    #main loop for newton's method
    s = initial_guess*1.0
    for k in range(kmax):
        sold = s
        s = .5*(s + x/s)
        if printhow == 1:
            print(k + 1, abs(s - sold))
        #check change in two successive steps for terminations
        if abs(s - sold) < tol:
            break
    return s


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def exp(x, printhow=0, initial_guess=1, kmax=100, tol=1e-14):
    if x < 0:
        return float('nan')
    
    s = initial_guess
    term = 1
    for k in range(kmax):
        sold = s
        term *= x / (k + 1)
        s += term
        if printhow == 1:
            print(k + 1, abs(s - sold))
        if abs(s - sold) < tol:
            break
    return s

def natualLog(x, printhow=0, initial_guess=0, kmax=100, tol=1e-14):
        if x <= 0:
            return float('nan')
        
        s = initial_guess
        for k in range(kmax):
            sold = s
            s += 2 * (x - exp(s)) / (x + exp(s))
            if printhow == 1:
                print(k + 1, abs(s - sold))
            if abs(s - sold) < tol:
                break
        return s
    

