# tv.py file
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self): 
        self.is_on = True 

    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def volume_up(self):
        if self.volume < 10:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

    def show_channels(self):
        print('Channel list:')
        count = 0
        for channel in self.channels:
            count += 1
            print(f"{count}. {channel}")

    def show_status(self):
        if self.is_on:
            if self.channel_no <= len(self.channels):
                name = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({name}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print("TV is off")

# tv_show.py file

def main():
    my_tv = TV()
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.show_channels()
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    my_tv.show_channels()
    my_tv.show_status()

    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "TVP Info"])
    my_tv.set_channel(4)
    my_tv.show_status()
    my_tv.set_channel(7)
    my_tv.show_status()
    my_tv.set_channel(10)        # poza zakresem - brak nazwy
    my_tv.show_status()

    for i in range(12):           # 12x volume_up, zeby sprawdzic limit 10
        my_tv.volume_up()
    my_tv.show_status()
    my_tv.volume_down()
    my_tv.show_status()

    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
   main()
