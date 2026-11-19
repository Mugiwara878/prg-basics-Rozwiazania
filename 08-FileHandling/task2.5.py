###
# Creates a shopping list based on product names entered from the keyboard
#
shopping_list = 'shopping_list.txt'

def add_product(file_name, product_name):
    with open(file_name, 'a') as file:    # 'a' = append, DOKŁADA na koniec (nie nadpisuje!)
        file.write(product_name + '\n')

product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break
    else:
        add_product(shopping_list, product)