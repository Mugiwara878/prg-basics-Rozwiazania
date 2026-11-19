###
# Calculates total cost of a shopping cart
#
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total = 0
for item, qty in cart.items():        # quantity
    total += prices[item] * qty      # cena * ilosc

print('Total cost:', round(total, 2))