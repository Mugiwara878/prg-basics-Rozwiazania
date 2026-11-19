###
# Summarizes hotel reservations from a JSON file
#
import json

def count_rooms(reservations):
    return len(reservations)              # liczba elementow listy = liczba rezerwacji

def count_paid(reservations):
    count = 0
    for r in reservations:
        if r['paid']:                      # True = oplacona
            count += 1
    return count

def count_unpaid(reservations):
    count = 0
    for r in reservations:
        if not r['paid']:                  # False = nieoplacona
            count += 1
    return count

def total_paid_value(reservations):
    total = 0
    for r in reservations:
        if r['paid']:
            total += r['nights'] * r['price_per_night']   # noce * cena za noc
    return total

def total_unpaid_value(reservations):
    total = 0
    for r in reservations:
        if not r['paid']:
            total += r['nights'] * r['price_per_night']
    return total

with open('reservations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

reservations = data['reservations']   # lista jest POD KLUCZEM "reservations"

print('Number of rooms:', count_rooms(reservations))
print('Number of paid reservations:', count_paid(reservations))
print('Number of unpaid reservations:', count_unpaid(reservations))
print('Total value of paid reservations:', round(total_paid_value(reservations), 2))
print('Total value of unpaid reservations:', round(total_unpaid_value(reservations), 2))