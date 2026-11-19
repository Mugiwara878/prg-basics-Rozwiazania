###
# Prints products with price less than 60 and stock less than 40
#
import csv

with open('clothing.csv', 'r') as file:
    # DictReader czyta CSV i zamienia kazdy wiersz w slownik
    # klucze = nazwy kolumn z naglowka (1 linia pliku), np. row['Price']
    reader = csv.DictReader(file)
    for row in reader:                            # row = jeden wiersz jako slownik
        price = float(row['Price'])               # wartosci z CSV to zawsze stringi, trzeba konwertowac
        stock = int(row['Stock_Quantity'])
        if price < 60 and stock < 40:
            print(row['Product_Name'], price, stock)