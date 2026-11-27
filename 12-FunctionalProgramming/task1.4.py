# Zadanie 1.4 - zamiana m/s na km/h (funkcja anonimowa)

# to samo co w 1.3, tylko zapisane jako lambda
ms_to_kmh = lambda ms: ms * 3.6

for speed in [10, 35]:
    # :g usuwa koncowke ".0"
    print(f"{speed} m/s = {ms_to_kmh(speed):g} km/h")
