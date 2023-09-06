#import dane
#import dane as dn
from dane import nrfilii as nf
from dane import book as bk

from funkcje.bfunkcje import czytaj_liste as cl, czytaj_slownik as cs

print("_____ dane ______")
print(nf)
print(bk)

print("_____ dane przez funkcje ______")
cl(nf)
print(".."*35)
cs(bk)
