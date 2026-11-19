###
# Separates even and odd numbers, even numbers first
#
arr = [7,9,2,4,5,6]
print('Before:', arr)

evens = []
odds = []
for val in arr:
    if val % 2 == 0:
        evens.append(val)
    else:
        odds.append(val)

result = evens + odds
print('After:', result)