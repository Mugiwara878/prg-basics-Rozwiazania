###
# Translates words from English to Polish using a dictionary
#
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('Enter an English word: ')
if word in translations:
    print(f'Translation: {translations[word]}')
else:
    print('Translation is unavailable.')