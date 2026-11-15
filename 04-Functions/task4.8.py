hours = int(input('Enter a hours: '))
minutes = int(input('Enter a minutes: '))
time_fromat= input('Enter a time formay: 12/24: ')
def time_string(hours, minutes, time_format):
    period = ''
    hour_12 = 0
    if time_fromat == '12':
        if hours == 0:
            hour_12 = 12
            period = 'am'
        elif hours < 12:
            hour_12 = hours
            period = 'am'
        elif hours == 12:
            hour_12 = 12
            period = 'pm'
        else:
            hour_12 = hours - 12
            period = 'pm'
        
        result = print(f"time is: {hour_12}:{minutes:02d}{period}") 
    
    if time_format =="24":
        result = print(f"time is: {hours}:{minutes:02d}")
    return result
time_string(hours, minutes, time_fromat)