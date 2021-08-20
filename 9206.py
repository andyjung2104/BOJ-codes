#9206
import math

def v(a,b,h):
    return (4*b*h**1.5+3*a*math.pi**.5*math.erf(h))/6
print(v(1,2,2),v(2,1,2))
