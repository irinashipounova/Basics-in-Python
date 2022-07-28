from random import choice
class Car:
    direction = ["N", "N-W", "N-E", "S", "S-W", "S-E", "E", "W"]
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Is {color} {name} a police car? Answer is {is_police}. \n  Why then does it go with {speed} km/h?")

    def go(self):
        print (f"{self.name} is going.")

    def stop(self):
        print (f"{self.name} has stopped.")

    def turn(self):
        print (f"{self.name} is turning {choice(self.direction)}.")

    def show_speed(self):
        print (f"{self.name} is going with {self.speed} km/h.")

class TownCar(Car):
    def show_speed(self):
        return f"{self.name} is going with {self.speed} km/h. {self.name} is going too fast!" if self.speed > 60 else super().show_speed()

class SportCar(Car):
    def show_speed(self):
        return f"{self.name} is going with {self.speed} km/h. Just because it can."

class WorkCar(Car):
    def show_speed(self):
        return f"{self.name} is going with {self.speed} km/h. {self.name} is going too fast!" if self.speed > 40 else super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police = True)

town_car = TownCar(60,'Blue','Lada')
work_car = WorkCar(40, 'Orange', 'KAMAZ')
sport_car = SportCar(120, 'Red', 'Ferrari')
police_car = PoliceCar(80, 'Blue and White', 'Ford')

Car_list = [town_car, work_car, sport_car, police_car]

for i in Car_list:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()