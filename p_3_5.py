def sum_func():
    s = 0
    while True:
        error = False
        num_list = input("Введите числа, разделенные пробелами, введите 'q', чтобы закончить: ").split()
        for num in num_list:
            if num.lower() == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    error = True
        if error:
            print('Данные неверны')
        print(f'Сумма введенных чисел = {s}')


print(sum_func())

