#przykład 1

def witaj(imie):
    return f'dziękujemy za założenie konta: {imie}'

def egzamin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, zaliczenie: {zaliczono}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(egzamin,"Nadia",45,True))




#przykład 2

def rejestracja(oplata):
    def lista_zawodnikow():
        return "jesteś na liście zawodników - opłata wzniesiona!"

    def brak():
        return "brak wpłaty - za 3 dni zostaniesz usunięty z listy."

    def error():
        return "błąd w kodzie opłaty: 1 - opłacono, 0 - brak, inna wartość to błąd!"

    if oplata == 1:
        return lista_zawodnikow()

    elif oplata == 0:
        return brak()

    else:
        return error()

print(rejestracja(1))
print(rejestracja(0))
print(rejestracja(12))

#przykład 3

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu")
        funkcja(*args)
        print("kończenie procesu")
    return wrapper


def zawijanie(czego):
    print(f'zawijanie {czego} w sreberka')

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na urodzinowym torcie!')

dmuchanie("świeczek")
