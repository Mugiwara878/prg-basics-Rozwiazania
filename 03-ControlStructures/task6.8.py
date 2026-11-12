name = input("Enter name: ")
name = name.lower()

if name[-1] == "a":
    name = name.capitalize()
    print(f"{name} -- Polish female name")
else:
    name = name.capitalize()
    print(f"{name} -- is not a Polish female name")