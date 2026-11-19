###
# Prints computer information from a JSON file
#
import json

with open('computer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)        # wczytaj JSON jako slownik

for key, value in data.items():   # przejdz po wszystkich parach klucz-wartosc
    print(key, ':', value)