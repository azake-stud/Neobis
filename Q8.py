len_array = int(input('Enter a  length of array: '))
in_count = 0
out_count = 0
for i in range(len_array):
    num = int(input(f'Enter {i+1}- number: '))
    if (num >= 10) and (num <= 20):
        in_count += 1
    else:
        out_count += 1
print(in_count, 'in')
print(out_count, 'out')



