price = input("Enter price: ")
price = float(price)
discount = input("Enter discount %: ")
discount = float(discount)
discount = (discount/100)
reduction = price*discount
price_with_discount = price - reduction
print(f"Price with discount: {round(price_with_discount,2)}")
print(f"Reduction: {round(reduction,2)}")