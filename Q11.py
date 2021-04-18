arr = []
for i in range(10):
    num = int(input('Enter a 10 numbers (positive or negative): '))
    if num <= 0:
        arr.append(1)
    else:
        arr.append(num)
for j in range(10):
    print(f"N[{j}] =", arr[j])
