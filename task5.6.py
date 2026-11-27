# Zadanie 5.6 - NAZWISKO wielkimi literami, przecinek, imie (map + lambda)

# kazda krotka to (nazwisko, imie)
employees = [("Smith", "Lucy"), ("Jones", "Janet"), ("Lee", "Jerry"),
             ("Jackson", "Peter"), ("Johnson", "Rick"),
             ("Lewis", "Terry"), ("Clarke", "Robin")]

# e[0] = nazwisko, .upper() zamienia na wielkie litery; e[1] = imie
result = list(map(lambda e: f"{e[0].upper()}, {e[1]}", employees))

for line in result:
    print(line)
