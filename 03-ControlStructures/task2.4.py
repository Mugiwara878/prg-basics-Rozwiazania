###
month = int(input('Enter month number (1..12): '))

if month >= 10 and month <= 12:
    quarter = 4
elif month >= 7 and month: 
    quarter = 3
elif month >= 4 and month:
    quarter = 2
elif month >= 1 and month:
    quarter = 1
else:
    quarter = 0
    print(f"Month number {month} does not exist")
    
if quarter > 0:
    print(f'Month {month} is in quarter {quarter}')