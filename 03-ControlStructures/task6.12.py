speed_limit_min = 40
speed_limit_max = 140
car_speed = int(input("Enter car speed: "))
if car_speed < speed_limit_min or speed_limit_max < car_speed:
    print("Warning: invalid car speed!!")
