def my_func():
    var_1 = int(input('Введите число: '))
    var_2 = int(input('Введите число: '))
    var_3 = int(input('Введите число: '))
    my_list = [var_1, var_2, var_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError, ValueError): #не срабатывает, я не смогла разобраться, почему!!!
        return 'Введите именно число!'

print(my_func())
