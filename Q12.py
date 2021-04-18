from random import *
num = [randint(0, 100000) for i in range(100)]
max_num = max(num)
print("Все рандомные числа (от 0 до 100'000) в количесиве 100 штук:", num)
print("Из них максимум это:", max_num)
print("Его позиция: ", num.index(max_num))




