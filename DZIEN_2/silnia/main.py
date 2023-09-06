#silnia: n! = 1*2*3*...*n
#double - > 1.8E+308
#dla silnii n>=0

import sys
from silniaerror import SilniaError

print(sys.version)

def silnia(n):
    if n<0:
        raise SilniaError(n)
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f'wynik funckji silnia dla n = {n} wynosi {silnia(n)}')
except SilniaError as info:
    print(info)
