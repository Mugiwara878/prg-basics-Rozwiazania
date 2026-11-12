# i = 0
# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f'{i+j}',end=' ')
#     print()

i = 6                      # i zaczyna od 6 (pierwszy rząd klawiatury: 7,8,9)
while i > -1:               # dopóki i > -1 (czyli i = 6, 3, 0 — trzy rzędy)
    j = 1                   # j resetuje się do 1 na początku KAŻDEGO rzędu
    while j < 4:             # dopóki j < 4 (czyli j = 1, 2, 3 — trzy kolumny)
        print(f'{i+j}', end=' ')  # wypisz i+j (np. dla i=6,j=1 → 7), bez nowej linii (end=' ')
        j += 1               # zwiększ j, żeby pętla wewnętrzna się kiedyś skończyła
    print()                  # po wypisaniu 3 liczb w rzędzie, przejdź do nowej linii
    i -= 3                   # zmniejsz i o 3, żeby przejść do następnego rzędu (6→3→0)