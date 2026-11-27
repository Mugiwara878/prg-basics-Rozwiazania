# Zadanie 5.13 - wykres slupkowy: ile medali razem zdobyl kazdy kraj
import matplotlib.pyplot as plt

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}]

# map nr 1: nazwy krajow -> os X
countries = list(map(lambda c: c["country"], medals))
# map nr 2: suma medali kazdego kraju -> wysokosc slupkow
totals = list(map(lambda c: c["gold"] + c["silver"] + c["bronze"], medals))

plt.bar(countries, totals)               # rysuje slupki
plt.title("Total number of medals won")  # tytul
plt.xlabel("Country")                    # opis osi X
plt.ylabel("Number of medals")           # opis osi Y
plt.show()                               # pokazuje wykres
