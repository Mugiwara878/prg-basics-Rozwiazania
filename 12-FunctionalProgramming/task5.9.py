# Zadanie 5.9 - miasta z dodatnia temperatura (filter + lambda na slowniku)

temps = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# filter na slowniku przechodzi po KLUCZACH, czyli po nazwach miast
# temps[city] wyciaga temperature danego miasta
positive = list(filter(lambda city: temps[city] > 0, temps))

# " ".join laczy nazwy miast spacjami
print("Cities with positive temperatures:", " ".join(positive))
