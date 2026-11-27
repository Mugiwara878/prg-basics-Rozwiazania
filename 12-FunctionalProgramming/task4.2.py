# Zadanie 4.2 - fotoradar, predkosci powyzej 50 km/h (filter + lambda)

speeds = [48, 47, 54, 50, 42, 68, 39, 46]

# zostawiamy tylko predkosci wieksze niz 50 (rowno 50 jest jeszcze dozwolone)
too_fast = list(filter(lambda s: s > 50, speeds))

# map(str, ...) zamienia liczby na tekst, a ",".join laczy je przecinkami
print("Recorded values:", ",".join(map(str, speeds)))
print("Speed too high:", ",".join(map(str, too_fast)))
