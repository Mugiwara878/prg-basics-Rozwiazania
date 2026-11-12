num = int(input("Enter a number: "))
og_num = num
bin = ''
while not num == 0:
    bin += str(num % 2)
    num = num // 2
    
bin = bin[::-1]
print(f"{og_num} = {bin}")
