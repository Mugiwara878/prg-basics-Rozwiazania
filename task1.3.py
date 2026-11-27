# Zadanie 1.3 - zamiana m/s na km/h (zwykla funkcja)
# 1 m/s = 3600 m na godzine = 3.6 km/h, wiec mnozymy przez 3.6

def ms_to_kmh(ms):
    return ms * 3.6

# petla przechodzi po dwoch predkosciach z przykladu
for speed in [10, 35]:
    # :g wyswietla liczbe bez zbednego ".0" (36 zamiast 36.0)
    print(f"{speed} m/s = {ms_to_kmh(speed):g} km/h")
