# Zadanie 5.11 - studenci z wynikiem od 50 do 70 pkt (filter + lambda)

# lista slownikow, kazdy slownik to jeden student
test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52}]

# s["result"] wyciaga wynik studenta; 50 <= x <= 70 sprawdza oba konce naraz
selected = list(filter(lambda s: 50 <= s["result"] <= 70, test_results))

for s in selected:
    print(f"{s['name']}: {s['result']} pts")
