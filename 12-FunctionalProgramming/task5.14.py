# Zadanie 5.14 - procent zle napelnionych butelek (filter + funkcja wyzszego rzedu)

# funkcja wyzszego rzedu: zwraca lambde, ktora sprawdza jedna butelke
def wrong_filling(capacity, tolerance):
    # 2% z 500 ml = 10 ml, czyli poprawnie jest od 490 do 510 ml
    margin = capacity * tolerance / 100
    # abs() to wartosc bezwzgledna: o ile ml butelka rozni sie od 500 (bez znaczenia czy w gore czy w dol)
    # True = roznica wieksza niz 10 ml, czyli butelka zle napelniona
    return lambda ml: abs(ml - capacity) > margin

capacity = 500
tolerance = 2
bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# filter zostawia tylko zle napelnione butelki: 512, 511, 476
wrong = list(filter(wrong_filling(capacity, tolerance), bottles))

# procent = zle / wszystkie * 100 -> 3 / 10 * 100 = 30
percent = len(wrong) / len(bottles) * 100

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {tolerance}%")
print(f"Filled bottles:     {','.join(map(str, bottles))}")
print(f"Incorrectly filled: {percent:.0f}%")
