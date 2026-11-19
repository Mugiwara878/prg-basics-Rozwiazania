###
# Counts the number of vowels in text entered from the keyboard
#
import re

text = input('Enter text: ')
vowels = re.findall(r'[aeiouAEIOU]', text)   # klasa znaków [...] - każda samogłoska, duża lub mała
print('Number of vowels:', len(vowels))