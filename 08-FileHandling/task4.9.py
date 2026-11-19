###
# Prints first name, last name and email of Graphic Designers, using the csv module
#
import csv

print('GRAPHIC DESIGNERS')
print('=================')

with open('it_company.csv', 'r') as file:
    reader = csv.DictReader(file)        # czyta CSV jako listę słowników: {kolumna: wartość}
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")