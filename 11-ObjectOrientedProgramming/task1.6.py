class Phone:
    def __init__(self,battery_level,is_on,volume):
        self.battery_level = battery_level
        self.is_on = is_on
        self.volume = volume

    def turn_on(self):
        self.is_on = True

    def charge(self, amount):
        self.battery_level += amount

    def set_volume(self):
        level = int(input("Enter a volume level: "))
        self.volume += level
       


def main():
    phone = Phone(
        45,True,20
    )
    phone.turn_on()
    phone.charge(27)
    phone.set_volume()
    print(f'Phone is on: {phone.is_on}, Battery: {phone.battery_level}, Volume: {phone.volume}')
    
    
    
if __name__ =="__main__":
    main()
        