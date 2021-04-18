def convert_to_oct(n):
    if n == 0:
        return '0'
    out = ""
    while n > 0:
        out += str(n % 8)
        n //= 8
    return out[::-1]


n1, n2 = int(input('Введите первое "десятичное число" :')), \
         int(input('Введите второе "десятичное число" :'))
print("Их сумма в 'десятичном СС' : ", n1 + n2)
print("Их сумма в 'восмеричном СС': ", convert_to_oct(n1 + n2))

