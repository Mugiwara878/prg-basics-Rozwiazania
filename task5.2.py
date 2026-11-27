# Zadanie 5.2 - suma liczb parzystych (filter + reduce + lambda)

# reduce nie jest wbudowane, trzeba je zaimportowac z modulu functools
from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

# krok 1: filter zostawia tylko liczby parzyste -> [2, 4, 6]
even = list(filter(lambda n: n % 2 == 0, numbers))

# krok 2: reduce laczy elementy po kolei w jeden wynik:
# 2 + 4 = 6, potem 6 + 6 = 12
total = reduce(lambda x, y: x + y, even)

print(f"Numbers: {numbers}")
print(f"Even numbers: {even}")
print(f"Sum of even numbers: {total}")
