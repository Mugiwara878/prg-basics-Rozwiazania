# Zadanie 3.2 - ile liter ma kazde slowo (map + lambda)

sentence = "I completely agree with you"

# split() tnie zdanie po spacjach na liste slow: ['I', 'completely', ...]
# map() dla kazdego slowa liczy len(), czyli liczbe liter
result = list(map(lambda word: len(word), sentence.split()))

print(f"Text: {sentence}")
print(f"No. of letters in words: {result}")
