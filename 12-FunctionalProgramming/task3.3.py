# Zadanie 3.3 - laczna wartosc towaru w magazynie (map + sum + lambda)

# kazda krotka to (ilosc sztuk, cena za sztuke)
stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# lambda dla kazdej krotki liczy ilosc * cena (item[0] * item[1])
# sum() dodaje wszystkie te wartosci do siebie
total = sum(map(lambda item: item[0] * item[1], stock))

print(f"Products in stock: {stock}")
print(f"Total value: {total:.2f}")
