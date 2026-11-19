###
# Counts occurrences of each word in a paragraph
#
paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()
counts = {}

for word in words:
    if word in counts:          # zwieksz
        counts[word] += 1
    else:                        #  dodaj nowy klucz do słownika
        counts[word] = 1

print(counts)