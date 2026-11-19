###
# Calculates the total number of hours in the winter semester
#
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

total = sum(winter_semester.values())   # suma WARTOŚCI słownika
print(f'The total number of hours in the winter semester is {total}')