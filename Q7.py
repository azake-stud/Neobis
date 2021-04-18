corr_parol = 2016
while True:
    parol = int(input("Please enter a pincode: "))
    if parol == corr_parol:
        print('Access permitted')
        break
    else:
        print('Incorrect password')

