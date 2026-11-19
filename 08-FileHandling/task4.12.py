###
# Copies book data to genre-specific files
#
import csv

def genre_filename(genre):
    if genre == 'Fantasy':
        return 'books_fantasy.txt'
    elif genre == 'Historical':
        return 'books_historical.txt'
    elif genre == 'Romance':
        return 'books_romance.txt'
    elif genre == 'Classic':
        return 'books_classic.txt'
    else:
        return None             # inne gatunki (np. Fiction) - pomijamy

def save_book(book):
    target_file = genre_filename(book['Genre'])
    if target_file:
        with open(target_file, 'a') as file:
            file.write(f"{book['Title']},{book['Author']},{book['Year']}\n")

with open('books.csv', 'r') as file:
    reader = csv.DictReader(file)
    for book in reader:
        save_book(book)

print('Done!')