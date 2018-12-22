#This program will solve for a triangle
from math import sqrt,tan,atan,radians,degrees,sin,asin,cos,acos,pi
def py(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if not a:
        a = sqrt(c**2 - b**2)
    elif not b:
        b = sqrt(c**2 - a**2)
    elif not c:
        c = sqrt(a**2 + b**2)
    return a,b,c
def right(a,b,c,A,B,C):
    if C == 90:
        if a:
            if b
    
