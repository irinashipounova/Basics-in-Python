my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

u = [el for el in my_list if my_list.count(el) == 1]

print(f"Initial list\n{my_list}\n Unique values\n{u}")
