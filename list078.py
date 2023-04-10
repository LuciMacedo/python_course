values_list = []
max_value = 0
min_value = 0
for num in range(0, 5):
    values_list.append(int(input(f'Type a number for the position {num}: ')))
    if num == 0:
        max_value = values_list[num]
        min_value = values_list[num]
    else:
        if values_list[num] > max_value:
            max_value = values_list[num]
        if values_list[num] < min_value:
            min_value = values_list[num]
print('*-' * 23)
print(f'You typed {values_list}')
print(f'The greatest number is {max_value} na position: ')
for i, v in enumerate(values_list):
    if v == max_value:
        print(f'{i + 1}...', end='')
print(f'The smallest number is {min_value} na position: ')
for i, v in enumerate(values_list):
    if v == min_value:
        print(f'{i + 1}', end='')



