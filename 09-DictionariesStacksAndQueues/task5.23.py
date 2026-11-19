###
# Displays last 10 EUR exchange rates from a JSON file
#
import json

with open('euro.json', 'r') as file:
    data = json.load(file)

print(f"{'Date':<15}{'Buying Rate':<15}{'Selling Rate':<15}")
print('=' * 45)
for rate in data['rates']:              # rates jest lista pod kluczem "rates"
    date = rate['effectiveDate']
    bid = rate['bid']                    # kurs kupna (bank KUPUJE od Ciebie)
    ask = rate['ask']                    # kurs sprzedazy (bank SPRZEDAJE Tobie)
    print(f"{date:<15}{bid:<15}{ask:<15}")