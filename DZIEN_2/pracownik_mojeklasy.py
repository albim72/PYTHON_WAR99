class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.koloroczu = "brązowe"

    def print_osoba(self):
        print(f'osoba -> imię: {self.imie}, wiek, lat: {self.wiek} , waga: {self.waga} kg,'
              f' wzrost: {self.wzrost} cm, kolor oczu: {self.koloroczu}')

    def czypracownik(self)->bool:
        return False

os1 = Osoba("Jan",34,99,173)
os1.print_osoba()
print(f'czy osoba jest pracownikiem? {os1.czypracownik()}')


class Firma:
    def __init__(self,nazwa,branza,miasto):
        self.nazwa = nazwa
        self.branza = branza
        self.miasto = miasto
        
    def show_firma(self):
        return f'firma {self.nazwa}, branża: {self.branza}, siedziba - miasto {self.miasto}'
        
        
        

