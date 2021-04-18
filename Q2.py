num = int(input("Введите число: "))
variant = 1
counter = 0
while variant < num:
  variant = variant * 2
  counter += 1
print("Количество попыток: ", counter)

