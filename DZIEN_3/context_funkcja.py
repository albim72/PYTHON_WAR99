from contextlib import contextmanager

@contextmanager
def context_string(string_input):
    print("Otworzenie managera... \n")

    swapped = string_input.swapcase()
    try:

        yield swapped
    except ValueError as e:
        print(f"błąd poboru danych... {e}")
    except Exception as exc:
        print(exc)
    finally:
        print("Zamknięcie działania...")

    print("Koniec działanie context managera!")

with context_string('wielkie i ważne wydarzenie roku: koncert grupy XYZ...') as sws:
    print(sws)

# with context_string(True) as sws:
#     print(sws)

str = "1 Maja"
print(str.upper())
