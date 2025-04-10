"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        math.sqrt(a)
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a, b): 
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
     if a == 0:
         raise ZeroDivisionError
     else:
         return b / a
def logarithm(a,b):
    if a >= 0 or a == 1 or b >= 0:
        raise ValueError
    else:
        math.log(b, a)

def exponeent(a,b):
    return a ** b
=======

import math
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        math.sqrt(a)
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm undefined for these values.")
    return math.log(b, a)

def exp(a, b):
    return a ** b
>>>>>>> cd2a490a21a5075a16b3a63dc69755bc33139026



