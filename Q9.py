import random
import math

num = [random.randint(1, math.pow(10, 100)) for i in range(int(input('Enter a quantity:')))]
#n1=[115380,2819311,23456]
for i in num:
    led_count = 0
    for j in str(i):
        if j == '2' or j == '3' or j == '5':
            led_count += 5
        elif j == '0' or j == '6' or j == '9':
            led_count += 6
        elif j == '1':
            led_count += 2
        elif j == '4':
            led_count += 4
        elif j == '7':
            led_count += 3
        elif j == '8':
            led_count += 7
    print(led_count, 'leds')

