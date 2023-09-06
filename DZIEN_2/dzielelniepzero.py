def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("nie dziel przez 0!")
    except NameError:
        print("zmienne niezdefiniowane")
    except Exception as ex:
        print(f'komunikat błędu: {ex}')
    else:
        print(f'wynik = {wynik}')
    finally:
        print("policzmy coś jeszcze!")

try:
    dzielenie(4,5)
    dzielenie(2,0)
    dzielenie(0.1,0.000023)
    dzielenie(0,0)
    dzielenie(-88,0.99)
    dzielenie(True,3)
    dzielenie(7,False)
    dzielenie("dfdskfs",False)
    dzielenie(45)
except TypeError as t:
    print(f"zbyt mało argumentów! -> {t}")
