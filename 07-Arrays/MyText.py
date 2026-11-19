###
# Module with text utility functions
#
def word_count(text):
    words = text.split()      # dzielimy tekst na listę słów (po spacjach)
    return len(words)         # zwracamy liczbę elementów tej listy

def words_by_length(text):
    words = text.split()
    # sortujemy wg długości słowa (key=len), od najdłuższego (reverse=True)
    return sorted(words, key=len, reverse=True)

def words_alphabetically(text):
    words = text.split()
    return sorted(words, key=str.lower)      # domyślne sortowanie stringów = alfabetycznie, key=str.lower porównuje wszystko tak jakby bylo pisane małą literą 