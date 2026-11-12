for row in range(1, 8):       # 7 rzędów (row = 1..7)
    for col in range(7):       # 7 kolumn w każdym rzędzie (col = 0..6)
        print(row + col*7, end=' ')  # wzór: numer = rząd + kolumna*7
    print()                    # nowa linia po każdym rzędzie