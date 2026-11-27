# Zadanie 1.1 - srednia arytmetyczna dwoch liczb (zwykla funkcja def)

# funkcja dostaje dwie liczby i zwraca ich srednia
def mean(x, y):
    return (x + y) / 2

# input() zwraca tekst, wiec int() zamienia go na liczbe calkowita
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# wywolujemy funkcje i zapisujemy wynik do zmiennej
result = mean(n1, n2)

# f-string wstawia wartosci zmiennych w {} do tekstu
print(f"The arithmetic mean of the numbers {n1} and {n2} is {result}")
