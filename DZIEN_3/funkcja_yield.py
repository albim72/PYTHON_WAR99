#funkcja generatorowa
#przypadek 1
def liczby():
    for i in range(11):
        yield i*2

#print(liczby())
for p in liczby():
    print(p)

#przypadek 2
def wznowienia(n,k):
    print("wstrzymania działania")
    yield 1000
    print("wznowienie działania...")

    print("wstrzymania działania")
    yield n+k
    print("wznowienie działania...")

    print("wstrzymania działania")
    yield n-k
    print("wznowienie działania...")

    print("wstrzymania działania")
    yield n*k
    print("wznowienie działania...")

    print("wstrzymania działania")
    yield n**k
    print("wznowienie działania...")

    print("wstrzymania działania")
    yield "ostatni!"
    print("wznowienie działania...")

for i in wznowienia(8,4):
    print(f'zwrócono wartość z yield: {i}')
