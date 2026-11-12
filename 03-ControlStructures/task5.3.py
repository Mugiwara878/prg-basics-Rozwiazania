###
total_sum = 0
counter = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
    counter += 1 
if counter == 0:
    print("you must provide at least one value!")
else:
    average = total_sum/counter
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The average of the numbers is: {average}")