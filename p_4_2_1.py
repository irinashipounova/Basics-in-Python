my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [num1 for num1, num2 in zip(my_list[1:], my_list[:-1]) if num1 > num2]

print(new_list)