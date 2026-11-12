time_24 = input('Enter time (24-hour formatcz): ')
hour = int(time_24[0:2])
minute = time_24[3:5]

if hour == 0:
    hour_12 = 12
    period = 'am'
elif hour < 12:
    hour_12 = hour
    period = 'am'
elif hour == 12:
    hour_12 = 12
    period = 'pm'
else:
    hour_12 = hour - 12
    period = 'pm'

print(f'Time in 12-hour format: {hour_12}:{minute}{period}')