len = int(input('Введите длину массива: '))
arr = [i for i in range(1, len+1)]
num = int(input('Введите число: '))
arr2 = [abs(j-num) for j in arr]
mesto = arr2.index(min(arr2))
print("Наиболее близкий вариант это: ", arr[mesto])

