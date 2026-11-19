###
# Records voting results in a JSON file
#
import json
import os

file_name = 'voting.json'

if os.path.exists(file_name):           # czy plik juz istnieje?
    with open(file_name, 'r') as file:
        votes = json.load(file)          # wczytaj JSON jako slownik
else:
    votes = {}                           # pierwszy raz - pusty slownik

person_name = input('Name of the person you are voting for: ')
votes[person_name] = votes.get(person_name, 0) + 1   # +1 glos (albo zacznij od 1)

with open(file_name, 'w') as file:
    json.dump(votes, file, indent=4)     # zapisz slownik jako JSON (indent=4 = ladne formatowanie)

print(votes)