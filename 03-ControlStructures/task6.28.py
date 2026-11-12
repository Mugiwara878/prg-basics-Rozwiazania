n = int(input("Enter N: "))  # ile liczb pierwszych chcemy znaleźć
count = 0                     # ile już znaleźliśmy
number = 2                    # od jakiej liczby zaczynamy sprawdzać (2 to pierwsza liczba pierwsza)

print("Prime numbers: ", end='')
while count < n:              # dopóki nie znaleźliśmy N liczb pierwszych
    is_prime = True            # zakładamy, że number JEST pierwsza, dopóki nie udowodnimy inaczej
    for divisor in range(2, number):  # sprawdzamy każdy możliwy dzielnik od 2 do number-1
        if number % divisor == 0:     # jeśli number dzieli się bez reszty...
            is_prime = False           # ...to NIE jest liczbą pierwszą
            break                      # nie ma sensu sprawdzać dalej, przerywamy pętlę wewnętrzną
    if is_prime:                # jeśli po sprawdzeniu wszystkich dzielników dalej jest "prime"
        print(number, end=' ')  # wypisz ją
        count += 1               # i zwiększ licznik znalezionych liczb pierwszych
    number += 1                  # przejdź do sprawdzenia następnej liczby