# przykład nr 1
import math

n=100
h=101
def g(x,z,y=3):
    n = x*math.sqrt(y) - z + n
    m = 2*z
    return n + m

print(g(5,5.6,2))
print(g(5,1.1))
print(g(y=1,x=8,z=3))
print(n)
