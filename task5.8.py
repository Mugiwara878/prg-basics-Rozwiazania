# Zadanie 5.8 - kto zdal przy roznych progach (filter + funkcja wyzszego rzedu)

# funkcja wyzszego rzedu: nie zwraca liczby, tylko INNA FUNKCJE (lambde)
# min_pts(70) zwraca lambde "czy pts >= 70", min_pts(40) zwraca "czy pts >= 40" itd.
def min_pts(limit):
    return lambda pts: pts >= limit

results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

# dla kazdego progu robimy nowa lambde i dajemy ja do filter()
for limit in [70, 40, 30]:
    passed = list(filter(min_pts(limit), results))
    print(f"Min {limit} pts: {passed}")
