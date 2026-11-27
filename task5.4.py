# Zadanie 5.4 - trzecia potega liczb od 1 do 20 (map + lambda)

# range(1, 21) daje liczby od 1 do 20 (21 juz nie wchodzi)
numbers = list(range(1, 21))

# ** to potegowanie, n ** 3 = n do trzeciej
cubes = list(map(lambda n: n ** 3, numbers))

print(cubes)
