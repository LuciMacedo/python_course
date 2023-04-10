number_list = []

while True:
    number_list.append(int(input('Type a number: ')))
    resp = str(input('Do you wanna continuous? [S/N] '))
    if resp in 'Nn':
        break
print('*-' * 24)
print(f'You typed {len(number_list)} times.')
number_list.sort(reverse=True)
print(f'Descending order is {number_list}')
if 5 in number_list:
    print('Number 5 is on the list')
else:
    print('There is no number 5 on the list')





