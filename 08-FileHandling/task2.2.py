###
# Writes Seven Wonders of the World to a file, alphabetically
#
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

file_name = 'seven_wonders.txt'

sorted_wonders = sorted(seven_wonders)   # sortowanie, znamy już z list

with open(file_name, 'w') as file:
    for item in sorted_wonders:
        file.write(item + '\n')          # każda nazwa + znak nowej linii