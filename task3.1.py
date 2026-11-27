# Zadanie 3.1 - przeliczenie transakcji z EUR na PLN (map + lambda)

transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]

# map() wykonuje lambde na KAZDYM elemencie listy (kazda kwota razy 4.5)
# map zwraca "obiekt map", wiec list() zamienia go na zwykla liste
transactions_in_pln = list(map(lambda x: x * 4.5, transactions_in_eur))

# wypisujemy kazda kwote z dwoma miejscami po kropce
for t in transactions_in_pln:
    print(f"{t:.2f}")
