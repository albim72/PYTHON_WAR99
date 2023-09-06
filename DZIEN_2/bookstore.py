class Book:
    # deklaracja stanu -> konstruktory
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)
    def __init__(self, idbk, tytul, autor, cena=30):
        self.idbook = idbk
        self.tytul = tytul
        self.autor = autor
        self._cena = cena
        self._oprawa = "miękka"
        self.create_book()

    #opis zachowania
    def create_book(self):
        print("utworzenie nowej książki")

    def print_book(self):
        print(f'książka: {self.tytul}, autor: {self.autor}, cena: {self._cena} zł, oprawa: {self._oprawa}')

    def rabat(self,procent):
        return self._cena*(procent/100)

    def get_cena(self):
        return self._cena

    def set_cena(self,nowa_cena):
        self._cena = nowa_cena

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self,nowacena):
        self._cena = nowacena
        self._oprawa = "twarda"


b1 = Book(45,"Wiedźmin","Andrzej Sapkowski",41)
print(b1)
b1.print_book()
print(b1._cena)
print(f'rabat od kwoty {b1.cena} zł wynosi {b1.rabat(12)} zł')
b1.cena = 48
print(f'rabat po zmianie od kwoty {b1.cena} zł wynosi {b1.rabat(12)} zł')

print(b1._cena)

b1.print_book()


print("_"*35)
b2 = Book(89,"Hobbit","J.R.R. Tolkien",38)
b2.print_book()
print(f'rabat od kwoty {b2.cena} zł wynosi {b2.rabat(12)} zł')
b2.cena = 44
print(f'rabat po zmianie od kwoty {b2.cena} zł wynosi {b2.rabat(12)} zł')

print(b2._cena)

b2.print_book()
print("_"*35)

b1.print_book()
