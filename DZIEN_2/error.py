try:
    print(x)
except NameError:
    print("x nie jest zdefiniowany!")
except TypeError:
    print("niewłaściwa wartość")
except:
    print("nieoczekiwany błąd")
else:
    print(f'podwójny x = {2*x}')
finally:
    print("policzmy ciąg dalszy!")

print("ciąg dalszy")
