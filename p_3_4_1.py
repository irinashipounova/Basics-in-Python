def my_func():
    a = int(input('Введите действительное положительное число: '))
    b = int(input('Введите целое отрицательное число: '))
    if a < 0 or b > 0:
        print('Error')
    else:
        return a ** b

print(my_func())