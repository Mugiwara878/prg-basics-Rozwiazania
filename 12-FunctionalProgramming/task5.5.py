# Zadanie 5.5 - liczby od 1 do 20 podzielne przez 2 i przez 3 (filter + lambda)

numbers = list(range(1, 21))

# n % 2 == 0 -> dzieli sie przez 2, n % 3 == 0 -> dzieli sie przez 3
# and -> oba warunki musza byc spelnione naraz
result = list(filter(lambda n: n % 2 == 0 and n % 3 == 0, numbers))

print(result)   # [6, 12, 18]
