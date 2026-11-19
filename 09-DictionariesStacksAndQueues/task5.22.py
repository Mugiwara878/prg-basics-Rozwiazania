###
# Saves product data entered from keyboard to a JSON file
#
import json

product = {}

product['name'] = input('Product name: ')
product['price'] = float(input('Price: '))             # float, nie string!
paid_input = input('Paid? (y/n): ')
product['paid'] = paid_input == 'y'                     # bool, nie string!

with open('product.json', 'w') as file:
    json.dump(product, file, indent=4)

print(product)