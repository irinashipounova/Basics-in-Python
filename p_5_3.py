with open('text_3.txt', 'r', encoding='utf-8') as sal:
    tab = {el.split()[0]: float(el.split()[1]) for el in sal}
    for key, value in tab.items():
        print (key, value)
av_sal = round(sum(tab.values()) / len(tab), 2)
print(f'Средняя зарплата сотрудников: {av_sal}')
print('Меньше 20000 получают: ')
for el in tab.items():
    if el[1] < 20000:
        print(el[0])
