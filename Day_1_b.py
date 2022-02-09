# 1
print(50 + 50)  # 100
print(100 - 10)  # 90

# 2
print(30+*6)  # Syntax error 
print(6^6)  # 0
print(6**6)  # 46656
print(6 + 6 + 6 + 6 + 6 + 6)  # 36

# 3
print("Hello World")
print("Hello World : 10")

# 4   If you are having trouble running this, run on Juypter Notebook.
from sympy.solvers import solve
from sympy import Symbol
import math

M = Symbol('M')

def function(P, R, L):
    if (L > 0):
        value = (P + (P * ((R/12) / 100))) - M
        return function(value, R, L - 1)
    else:
        return P
    
def mortgage(P, R, L):
    return math.ceil(solve(function(P, R, L), M)[0])

print(mortgage(800000, 6, 103))  # 9957