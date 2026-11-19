###
# Checks the correctness of username and password
#
import re

username = input('Enter username: ')
password = input('Enter password: ')

# ^[a-z]{6,}$ = od początku(^) do końca($) STRING, 6 lub więcej (6,) małych liter a-z
username_pattern = r'^[a-z]{6,}$'
# ^[A-Za-z0-9_]{8,}$ = 8+ znaków, tylko litery (duże/małe), cyfry, podkreślnik
password_pattern = r'^[A-Za-z0-9_]{8,}$'

username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

if username_match and password_match:
    print('Username and password are correct')
else:
    print('Username or password is incorrect')