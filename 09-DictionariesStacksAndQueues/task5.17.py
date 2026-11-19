###
# Prints information about cities from a JSON array
#
import json

with open('cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)         # lista slownikow

for city in data:                  # kazdy element listy to jeden slownik (jedno miasto)
    for key, value in city.items():
        print(key, ':', value)
    print()                        # pusta linia miedzy miastami
