###
# Finds the most expensive expense category
#
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = 0
for i in range(len(expenses)):
    if expenses[i] > expenses[max_index]:
        max_index = i

print(f'The most expensive category is {categories[max_index]} with {expenses[max_index]}')