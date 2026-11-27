# Zadanie 5.7 - skoki narciarskie: suma not bez najwyzszej i najnizszej

# kazda krotka to 5 not od sedziow dla jednego zawodnika
scores = [(17, 15, 16, 17, 15),
          (16, 18, 19, 17, 19),
          (19, 15, 15, 19, 18),
          (18, 17, 19, 15, 16)]

# dla kazdego zawodnika: suma wszystkich not minus najwyzsza (max) minus najnizsza (min)
# zostaja 3 srodkowe noty
result = list(map(lambda s: sum(s) - max(s) - min(s), scores))

print(result)   # [48, 54, 52, 51]
