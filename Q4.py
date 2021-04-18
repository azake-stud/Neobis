len = int(input('Введите длину массива: '))
arr = [i for i in range(1, len + 1) if 0 < i < 1000]
num = [int(input('Введите число:')), int(input('Укажите место:'))]
print(f"Массив до {len}:\n", arr)
arr.insert(num[1]-1, num[0])
print("Измененный массив\n", arr)


