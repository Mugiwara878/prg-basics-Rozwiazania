###
# Counts registered vehicles per province, based on plate first letter
#
import csv

provinces = {}
with open('province.csv', 'r', encoding='utf-8') as file:   # utf-8 bo sa polskie znaki
    reader = csv.DictReader(file)
    for row in reader:
        provinces[row['Letter']] = row['Name']

counts = {}
with open('vehicle.txt', 'r') as file:
    for line in file:
        plate = line.strip()
        if plate == '':
            continue
        letter = plate[0]
        if letter in provinces:
            name = provinces[letter]
            counts[name] = counts.get(name, 0) + 1   # .get(klucz, 0) = wartosc albo 0 gdy brak klucza

for province, count in counts.items():
    print(f'{province}: {count}')