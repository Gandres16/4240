import math as np
import myfuncs as my

def test_math():
    print("this is using math module")
    print(np.sqrt(5))
    print(np.log(5))
    print(np.exp(2))
    print(np.factorial(5))
    print("")

def test_myfuncs():
    print("this is using myfuncs module")
    print(my.sqrt(5))
    print(my.natualLog(5))
    print(my.exp(2))
    print(my.factorial(5))

test_math()
test_myfuncs()