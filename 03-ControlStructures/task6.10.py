current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price:"))
reduced = (1 - current_price/previous_price) *100 
if reduced >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {round(reduced,2)}%")