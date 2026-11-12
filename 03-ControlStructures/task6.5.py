park_time = int(input("Enter parking hours: "))
if park_time <= 2:
    print("Please pay 5 zł.")
elif park_time <= 6:
    print("Please pay 15 zł.")
else:
    print("Please pay 20 zł.")
