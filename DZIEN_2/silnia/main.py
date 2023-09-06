#silnia: n! = 1*2*3*...*n
#double - > 1.8E+308
#dla silnii n>=0

import sys
from silniaerror import SilniaError

print(sys.version)
sys.set_int_max_str_digits(0x1000000)
sys.setrecursionlimit(0x2000000)

def silnia(n):
    if n<0:
        raise SilniaError(n)
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n<0:
        raise SilniaError(n)
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)


try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f'wynik funckji silnia dla n = {n} wynosi {silnia(n)}')
    print(f'wynik funckji rekurencyjnej silnia dla n = {n} wynosi {silnia_rek(n)}')
except SilniaError as info:
    print(info)
