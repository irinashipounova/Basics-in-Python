class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def surface_mass(self, m=25, h=5):
        m = int(input('Введите массу асфальта, необходимую для покрытия 1 кв.м. дороги  '))
        h = int(input('Введите требуемую толщину полотна в см '))
        surface_mass = m * h * self._length * self._width / 1000
        return surface_mass


a = Road(5000, 20)
print(a.surface_mass())
