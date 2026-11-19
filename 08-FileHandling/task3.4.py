###
# Calculates the total value of money spent
#
import re

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# r'...' = raw string, nie interpretuj znaków specjalnych w tym stringu
# € = dosłowny znak euro, ma wystąpić w tym miejscu
# \d = jedna cyfra (0-9), to skrót dla [0-9]
# + = "jeden lub więcej razy" poprzedniego elementu, czyli \d+ = cały ciąg cyfr (liczba)
# (...) = grupa przechwytująca - z całego dopasowania (€102) zwróć tylko to co w nawiasie (102)
pattern = r'€(\d+)'

amounts = re.findall(pattern, email)   # lista wszystkich dopasowanych liczb (jako stringi), np. ['102','30','15','20']

total = 0
for amount in amounts:
    total += int(amount)     # string -> int

print('Total spent:', total)