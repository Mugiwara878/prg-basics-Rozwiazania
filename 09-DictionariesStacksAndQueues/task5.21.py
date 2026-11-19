###
# Writes a favorite book/movie dictionary to a JSON file
#
import json

favourite = {
    "title": "Dżuma",
    "author": "Albert Camus",
    "year": 1947,
    "genre": "Philosophical novel",
    "pages": 308
}

with open('favourite.json', 'w') as file:
    json.dump(favourite, file, indent=4)
    # mozna dodac ensure_ascii=False, zeby polskie znaki (np. "ż") zapisaly sie dosłownie, nie jako \u017c

print('Saved to favourite.json')