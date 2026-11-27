# Zadanie 1.5 - srednia predkosc pojazdu (zwykla funkcja)

def avg_speed(distance, hours, minutes):
    # zamieniamy caly czas na godziny, np. 1 h 23 min = 1 + 23/60 = 1.383 h
    time = hours + minutes / 60
    # predkosc = droga / czas
    return distance / time

# float() bo dystans moze byc z przecinkiem, godziny i minuty to liczby calkowite
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# :.1f = wynik z jedna cyfra po kropce
print(f"Average speed: {avg_speed(distance, hours, minutes):.1f} km/h")
