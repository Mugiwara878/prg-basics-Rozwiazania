number_of_produt = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))
amount = 0
prom = 0.25
if number_of_produt > 2:
    amount = (number_of_produt-2)*(product_price-product_price*prom) + 2*product_price
else:
    amount = number_of_produt * product_price
print(f"Amount to pay: {amount}")