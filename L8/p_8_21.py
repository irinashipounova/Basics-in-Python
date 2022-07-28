a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    res = a / b
except ZeroDivisionError:
    print('На ноль делить нельзя!')
    b1 = int(input('Введите делитель, отличный от нуля: '))
    res = a / b1
    print(f'Результат деления {res}')
else:
    print(f'Результат деления {res}')

