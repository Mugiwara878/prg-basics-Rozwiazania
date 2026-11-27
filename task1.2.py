# Zadanie 1.2 - srednia arytmetyczna, ale jako funkcja anonimowa (lambda)

# pobieramy dwie liczby z klawiatury i zamieniamy tekst na int
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# lambda = funkcja w jednej linijce, bez def i bez return
# przed dwukropkiem argumenty (x, y), po dwukropku to, co zwraca
mean = lambda x, y: (x + y) / 2

# lambde wywolujemy tak samo jak zwykla funkcje
result = mean(n1, n2)
print(f"The arithmetic mean of the numbers {n1} and {n2} is {result}")
