class Book:
    # deklaracja stanu -> konstruktory
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)
    def __init__(self, idbk, tytul, autor, cena=30):
        self.idbook = idbk
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #opis zachowania
    def create_book(self):
        print("utworzenie nowej książki")

    def print_book(self):
        print(f'książka: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}')

    def rabat(self,procent):
        return self.cena*(procent/100)

    def get_cena(self):
        return self.cena

    def set_cena(self,nowa_cena):
        self.cena = nowa_cena


b1 = Book(45,"Wiedźmin","Andrzej Sapkowski",41)
print(b1)
b1.print_book()
print(f'rabat od kwoty {b1.get_cena()} zł wynosi {b1.rabat(12)} zł')
b1.set_cena(47)
print(f'rabat po zmianie od kwoty {b1.cena} zł wynosi {b1.rabat(12)} zł')


