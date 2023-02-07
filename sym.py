from math import *
from sympy import *
from sympy.plotting import plot

x = symbols('x')
fx = -12*x**4-18*x**3+5*x**2+10*x-30


# корни
print(solve(fx))

