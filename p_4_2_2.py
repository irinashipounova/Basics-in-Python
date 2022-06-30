from random import randint

ml = [randint(0, 500) for _ in range(0, randint(1,50))]
#result_list = [num for i, num in enumerate(ml[1:]) if num > ml[i]]
result_list = [num1 for num1, num2 in zip(ml[1:], ml[:-1]) if num1 > num2]

print(ml)
print(result_list)