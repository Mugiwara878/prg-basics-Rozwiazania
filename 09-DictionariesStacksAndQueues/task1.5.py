###
# Array of dictionaries with country and population
#
countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":83000000},
    {"name":"France", "population":68000000},
    {"name":"Spain", "population":47000000},
    {"name":"Italy", "population":59000000}
]

print(f"{'COUNTRY':<10}{'POPULATION':>12}")
for country in countries:
    print(f"{country['name']:<10}{country['population']:>12}")