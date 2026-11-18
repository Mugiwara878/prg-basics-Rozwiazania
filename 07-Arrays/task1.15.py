###
# Sorts an array using the bubble sort algorithm
#
def bubble_sort(arr):
    n = len(arr)                          # n = liczba elementów w tablicy
    for i in range(n):                    # zewnętrzna pętla: ile "przebiegów" po tablicy
        for j in range(n-i-1):            # wewnętrzna pętla: porównujemy sąsiednie pary
            if arr[j] > arr[j+1]:         # jeśli element jest większy od sąsiada z prawej
                arr[j], arr[j+1] = arr[j+1], arr[j]   # zamień je miejscami
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)