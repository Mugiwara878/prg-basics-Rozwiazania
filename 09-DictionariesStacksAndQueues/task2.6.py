###
# Merges contacts and removes duplicates using set union
#
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = contacts_A | contacts_B   # suma: wszystko z OBU zbiorów, bez duplikatów
print("Merged contacts:", merged_contacts)

# Operatory na zbiorach (set):
# |  = suma (union) - wszystko z obu zbiorow, bez duplikatow
# &  = czesc wspolna (intersection) - co jest w OBU zbiorach naraz
# -  = roznica (difference) - co jest w pierwszym, a nie ma w drugim
# ^  = roznica symetryczna - co jest w jednym LUB drugim, ale NIE w obu naraz
# setow NIE mozna laczyc operatorem + (TypeError)