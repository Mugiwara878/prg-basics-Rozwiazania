plain_text = 'The early bird catches the worm'
encrypted_text = ''
encrypted_character = ''
cesar = ''

for char in plain_text:
    # read the character's code (use ord())
    cesar = ord(char)
    # add one to the character's code
    cesar = cesar +1
    # replace new character code with its corresponding character (use chr())
    encrypted_character = chr(cesar)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + encrypted_character

print(plain_text)
print(encrypted_text)