numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
while True:
    user_input = int(input('Type a number between 0 to 20: '))
    if 0 <= user_input <= 20:
        break
    print('Try again')
print(f'You typed number {numbers[user_input]}')
