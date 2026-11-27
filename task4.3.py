# Zadanie 4.3 - srednia ocen bez ocen niedostatecznych 2.0 (filter + lambda)

grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

# zostawiamy tylko oceny rozne od 2.0
positive = list(filter(lambda g: g != 2.0, grades))

# srednia = suma ocen / ile ich jest
mean = sum(positive) / len(positive)

# :.2f zaokragla do 2 miejsc (27/7 = 3.857... -> 3.86)
print(f"Arithmetic mean for grades <> 2.0 is {mean:.2f}")
