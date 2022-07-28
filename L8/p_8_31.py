list_1 = []


class NotNumber(ValueError):
    pass


while True:
    try:
        num = input('Введите число: ')
        if num == 'end':
            print(f'{list_1}')
            break
        if not num.isdigit():
            raise NotNumber(num)

        num = int(num)
        list_1.append(num)
    except NotNumber:
        print('Это не число!')
