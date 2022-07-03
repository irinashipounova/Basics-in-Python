from random import randint

with open('new_file_5_5.txt', 'w', encoding='utf-8') as n_f5:
    my_list = [randint(1, 200) for _ in range(100)]
    n_f5.write(' '.join(map(str, my_list)))
    s = sum(my_list)

print(f'Сумма элементов в файле = {s}')
