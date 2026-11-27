# Zadanie 5.12 - kraje z co najmniej 10 medalami (filter + lambda)

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}]

# suma zlota + srebra + brazu musi byc >= 10
top = list(filter(lambda c: c["gold"] + c["silver"] + c["bronze"] >= 10, medals))

print("COUNTRIES WITH AT LEAST 10 MEDALS")
for c in top:
    print(f"{c['country']}: {c['gold']},{c['silver']},{c['bronze']}")
