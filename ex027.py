from random import choice
print('I will pick a number between 0 to 5. Try to guess!')
print('--='*20)
num = [0, 1, 2, 3, 4, 5]
computer_number = choice(num)
user_answer = int(input('Try to guess the number?'))
print('Loading...')
print('Congrats you won!' if computer_number == user_answer else 'I won!')