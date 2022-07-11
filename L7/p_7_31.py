class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number / other.number)

    def make_order(self, in_row_num):
        return '\n'.join(["\U0001f600" * in_row_num for _ in range (self.number // in_row_num)]) + '\n' + "\U0001f600" * (self.number % in_row_num)


num_1 = Cell(int(input('Enter the number of wells in the cell 1: ')))
num_2 = Cell(int(input('Enter the number of wells in the cell 2: ')))
in_row_1 = int(input('Enter the number of wells in the row for the cell 1: '))
in_row_2 = int(input('Enter the number of wells in the row for the cell 2: '))


print(f'Cell 1 + cell 2 will have {num_1 + num_2} wells in sum')
print(f'Cell 1 without cell 2 will have {num_1 - num_2} wells after subtraction')
print(f'Cell 1 * cell 2 will have {num_1 * num_2} wells after multiplication')
print(f'Cell 1 / cell 2 will have {num_1 / num_2} wells after division\n')

print(num_1.make_order(in_row_1),'\n')
print(num_2.make_order(in_row_2))