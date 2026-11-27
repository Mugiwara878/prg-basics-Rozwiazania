# Zadanie 1.6 - srednia predkosc pojazdu (funkcja anonimowa)

# lambda liczy: droga / (godziny + minuty zamienione na godziny)
avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60)

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# :.1f = jedna cyfra po kropce
print(f"Average speed: {avg_speed(distance, hours, minutes):.1f} km/h")
