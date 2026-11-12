age = int(input(("Enter age: ")))
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("You don't exist")