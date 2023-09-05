print("testujemy interpreter PY")
a = 65
print(a)
print(type(a))

a = "zielone"
print(a)
print(type(a))

b:float = 9.32534
print(b)
print(type(b))

b = "abc"
print(b)
print(type(b))

imiona = ["Jan","Monika","Leon","Olaf","Halina","Jan","Nadia","Maria","Leon"]

print(imiona)
print(imiona[0])
print(imiona.count("Jan"))
print(imiona.index("Jan"))
print(imiona[2:6])

#imiona2 = imiona[:]
imiona2 = list(imiona)
imiona2.sort()
print(imiona2)
print(imiona)

imionaparz = imiona[::2]
print(imionaparz)

im2 = imiona[2]
print(im2)

print(im2[::-1])

for nm in imiona:
    print(nm)

#krotka

miasta = ("Kraków","Lublin","Warszawa","Wrocław","Kraków","Kielce")
print(miasta)
print(type(miasta))

print(miasta.index("Lublin"))
print(miasta[2:5])

miasta_arr = list(miasta)
print(miasta_arr)
print(type(miasta_arr))

miasta_arr.insert(3,"Rzeszów")
print(miasta_arr)

miasta = tuple(miasta_arr)

print(miasta)

#set (zbiór)
kolory = {"zielony","biały","czerwony","niebieski","brązowy","zielony","zielony"}

print(kolory)
print(kolory)
print(kolory)

for k in kolory:
    print(k)

#print(kolory[2])

kolory.remove("biały")
print(kolory)


kolory.discard("czerwony")
print(kolory)

#słownik (dictionary)

osoba = {
    "imię":"Jan",
    "nazwisko":"Kot",
    "wiek":56,
    "miasto":"Rzeszów",
    "kierowca":True
}

print(osoba)
print(type(osoba))

print(osoba["imię"])

osoba["miasto"] = "Sanok"
print(osoba["miasto"])

osoba["zawód"] = "programista"
print(osoba)


print(osoba.keys())
print(osoba.values())
print(osoba.items())

print("____________ klucze ____________");
for x in osoba:
    print(x)

print("____________ Wartości ____________");
for x in osoba:
    print(osoba[x])
print("____________ Wartości ____________");
for y in osoba.values():
    print(y)

print("____________ Pary(klucz,wartość) ____________");
for x,y in osoba.items():
    print(f'klucz -> {x}: {y}')
