print((lambda e:e+2)(6))
b = lambda u,w:2*u/w

print(b(5,7.7))

c = lambda a,b,c=4:(a+b)*c if a>9 else 200

print(c(11,7,1.2))
print(c(2,2))

def multi(n):
    return lambda a:a+n

print(multi(5.6)(4))
