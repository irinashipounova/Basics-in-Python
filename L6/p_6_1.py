import time
from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        color = 'red'
        print(color)
        time.sleep(7)
        color = 'yellow'
        print(color)
        time.sleep(2)
        color = 'green'
        print(color)
        time.sleep(10)
a1 = TrafficLight('red')
a1.running()
