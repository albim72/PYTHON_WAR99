liczby = [56,90,88,100,45,0,194,888,1998,2013,0,3456,100,-34,456,-678,-1235,2,5,6]


def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    sr_arytm = suma_el/liczba_el

    return minimum, maksimum, rozstep, liczba_el, suma_el, sr_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,le,sm,sa = pokaz_statystyki(liczby)
print(f'wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, liczba elementów: {le},'
      f'suma wszystkich elementów: {sm}, średnia arytmetyczna: {sa}')
