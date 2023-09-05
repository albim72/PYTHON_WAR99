print((lambda e:e+2)(6))
b = lambda u,w:2*u/w

print(b(5,7.7))

c = lambda a,b,c=4:(a+b)*c if a>9 else 200

print(c(11,7,1.2))
print(c(2,2))

def multi(n):
    return lambda a:a+n

print(multi(5.6)(4))


liczba = [3,12,5,88,9,1,14,117,-4,0,24,-33,1,999,190,-45,101,1]

parz = list(filter(lambda x:x%2==0,liczba))
print(parz)

cube = list(map(lambda x:x**3,liczba))
print(cube)

cube_s = set(map(lambda x:x**3,liczba))
print(cube)

nums = [k**4-3 for k in range(1000000)]
print(nums)

numsz = {k**4-3 for k in range(1000000)}
print(numsz)

