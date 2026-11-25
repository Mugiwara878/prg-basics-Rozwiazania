# tv_show.py file
from tv import TV

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