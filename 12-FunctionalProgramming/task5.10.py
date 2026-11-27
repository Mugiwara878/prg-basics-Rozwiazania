# Zadanie 5.10 - wykres slupkowy temperatur w miastach
# matplotlib trzeba miec zainstalowane: pip install matplotlib
import matplotlib.pyplot as plt

temps = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# temps.items() daje pary (miasto, temperatura)
# pierwszy map bierze z kazdej pary nazwe miasta (item[0]) -> os X
cities = list(map(lambda item: item[0], temps.items()))
# drugi map bierze temperature (item[1]) -> wysokosc slupkow
values = list(map(lambda item: item[1], temps.items()))

plt.bar(cities, values)                     # rysuje slupki
plt.title("Temperatures recorded in cities")  # tytul wykresu
plt.xlabel("City")                          # opis osi X
plt.ylabel("Temperature [°C]")              # opis osi Y
plt.show()                                  # otwiera okno z wykresem
