# Zadanie 1.7 - lambda sprawdzajaca, czy liczba jest parzysta

# % to reszta z dzielenia; liczba parzysta ma reszte 0 przy dzieleniu przez 2
# porownanie == zwraca True albo False
is_even = lambda number: number % 2 == 0

# testujemy lambde na kilku liczbach
for n in [4, 7, 0, 13, 28]:
    print(f"{n} -> {is_even(n)}")
