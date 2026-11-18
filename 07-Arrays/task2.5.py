###
# Cinema seating information
#
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]
def seats_total(seats):
    return len(seats) * len(seats[0])

def seats_available(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                count += 1
    return count

def seats_booked(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                count += 1
    return count

def seat_status(seats, row, place):
    return seats[row-1][place-1]