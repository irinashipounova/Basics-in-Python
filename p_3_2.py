def my_func(**kwargs):
    return kwargs
n = input('Введите ваше имя: ')
y = input('Введите ваш год рождения: ')
t = input('Введите ваш город проживания: ')
e = input('Введите ваш e-mail: ')
p = input('Введите номер вашего телефона: ')

print(my_func(имя = n, год_рождения = y, город_проживания = t, email = e, телефон = p))
