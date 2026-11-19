###
# Modifies and displays a dictionary with mixed value types
#
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],      # wartość to LISTA!
    "married": True,                          # wartość to bool
    "phone": {"landline": "123444321", "mobile": "777888999"}   # wartość to SŁOWNIK (zagnieżdżony!)
}

print('Name:', person["name"])
print('Hobby:', person["hobby"])
print('Full dictionary:', person)

person["surname"] = "Nowak"
person["married"] = not person["married"]       # odwraca True/False
person["gender"] = "male"                         # nowy klucz - dodaje
person["hobby"].append("bicycle")                  # dokłada do LISTY wewnątrz słownika
person["phone"]["work"] = "313131444"               # dokłada do SŁOWNIKA wewnątrz słownika

print('Full dictionary (updated):')
for key, value in person.items():
    print(f"{key} : {value}")