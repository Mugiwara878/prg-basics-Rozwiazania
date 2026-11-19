###
# Prints the text and counts the number of words
#
with open('pets.txt', 'r') as file:
    total_words = 0
    for line in file:
        print(line, end="")
        words_in_line = len(line.split())
        total_words += words_in_line

print()
print('Total number of words:', total_words)