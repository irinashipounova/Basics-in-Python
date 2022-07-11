from itertools import cycle
my_list = [2, 4, 6, 8, 10, 8, 6, 4, 2]
i = 0
for el in cycle(my_list):
    if i > 18:
        break
    else:
        print(el)
    i += 1
