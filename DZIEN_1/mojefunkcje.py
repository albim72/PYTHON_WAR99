# przykład nr 1
import math

n=100
h=101

def h(x):
    return 3*x
def g(x,z,y=3):
    global n
    n = x*math.sqrt(y) - z + n
    m = 2*z + h(z)
    return n + m

print(g(5,5.6,2))
print(g(5,1.1))
print(g(y=1,x=8,z=3))
print(n)

# przykład 2

def ranking(*lang,nrrank,**noweargs):
    print(f'ranking nr {nrrank} -> pierwsze miejsce: {lang[0]}, drugie miejsce: {lang[1]},'
          f'trzecie miejsce: {lang[2]}')

def rankingk(k,nrrank):
    print(f'ranking nr {nrrank} -> pierwsze miejsce: {k[0]}, drugie miejsce: {k[1]},'
          f'trzecie miejsce: {k[2]}')


ranking("Python","Java","C#","JavaScript",nrrank=34,a=45)

lg = ("Python","Java","C#","JavaScript")
rankingk(lg,4)

rankingk("Python",45)


