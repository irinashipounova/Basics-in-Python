class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"

class Pen(Stationary):
    def draw(self):
        return f"{self.title} хороша для четкого контура"

class Pencil(Stationary):
    def draw(self):
        return f"{self.title} отлично штрихует"

class Handle(Stationary):
    def draw(self):
        return f"{self.title} обладает насыщенным цветом"

something = Stationary('Charcoal')
pen = Pen('Lamy')
pencil = Pencil('Faber-Castell')
marker = Handle('Copic')

new_list = [something, pen, pencil, marker]
for i in new_list:
    i.draw()
    print(i.draw())
