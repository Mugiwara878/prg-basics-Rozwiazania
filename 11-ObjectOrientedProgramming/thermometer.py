import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        self.temperature = round(random.uniform(34.0, 42.0), 1)

    def show_temperature(self):
        message = f'Temperature: {self.temperature}C'
        if self.temperature >= 41.0:
            message += ' (CRITICAL TEMPERATURE!!)'
        elif self.temperature >= 37:
            message += ' (fever)'
        print(message)


