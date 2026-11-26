from statistics_class import Statistics

stats = Statistics()
for n in [12, 37, 6, 9, 17]:
    stats.add_number(n)

stats.show_numbers()
stats.show_statistics()