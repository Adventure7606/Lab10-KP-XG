"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)
def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return b / a

def logarithm(a, b):
    if a <= 0 or b == 1 or b <= 0:
        raise ValueError("Logarithm undefined for these values.")
    return math.log(b, a)

def exp(a, b):
    return a ** b



