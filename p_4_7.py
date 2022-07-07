from math import factorial
def fact(n):
    return factorial(n)
n = int(input("Enter a number: "))
for i in range(0, n + 1):
    print(f'{i}! is {fact(i)}')
    n += 1
#работает, но не тем способом, которым надо было((