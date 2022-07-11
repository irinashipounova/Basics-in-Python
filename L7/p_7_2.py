from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def length(self):
       pass
    def __add__(self, other):
        return self.length + other.length

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def length(self):
        return float((self.size * 6.5) + 0.5)


class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def length(self):
        return float((self.height * 2) + 0.3)

cs = Coat(int(input('Enter your size: ')))

sh = Suit(float(input('Enter your height in meters: ')))

print(f'You need {cs + sh} meters of fabric')
