amount = int(input("Enter the amount in PLN: "))
og_amount = amount
coin_5 = 0
coin_2 = 0
coin_1 = 0

coin_5 += amount // 5
amount = amount % 5
coin_2 += amount // 2
amount = amount % 2
coin_1 += amount //1

print(f"The amount of PLN {og_amount} in coins: \n"
      f"5 PLN coins: {coin_5} \n"
      f"2 PLN coins: {coin_2} \n"
      f"1 PLN coins: {coin_1}")