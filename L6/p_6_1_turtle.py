import time
from time import sleep

import turtle

class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        t = turtle.Pen()
        t.pencolor("red")
        t.circle(100)
        t.left(90)
        time.sleep(7)
        t.pencolor("yellow")
        t.circle(100)
        t.left(90)
        time.sleep(2)
        t.pencolor("green")
        t.circle(100)
        t.left(91)
        time.sleep(10)
a1 = TrafficLight('red')
a1.running()
