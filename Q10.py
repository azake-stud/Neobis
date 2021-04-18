def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


len_fibo = int(input('Please enter a length of fibonacci numbers: '))
if len_fibo <= 0:
    print("Please enter a positive number: ")
else:
    print("Fibonacci numbers are:")
    for i in range(len_fibo):
        print(f'Fib({i+1}) =', fibo(i))
