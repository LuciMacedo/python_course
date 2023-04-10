number_list = []
even_list = []
odd_list = []
while True:
    number_list.append(int(input('Type a number: ')))
    user_input = str(input('Do you wanna continuous? [s/n]'))
    if user_input in 'Nn':
        break
print(f'The full list is {number_list}')

for num in number_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(f'Odd numbers are {odd_list}')
print(f'The even numbers are {even_list}')




