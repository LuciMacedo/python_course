number = int(input('Type a number: '))
print('''pick one option:
      [1] bi
      [2] octal''')
choice = int(input('Type your option:'))
if choice == 1:
    print('The number {} converted to bi is {}'.format(number, bin(number)[2:]))
elif choice == 2:
    print('The number {} converted to oc is {}'.format(number, oct(number)[2:]))
else:
    print('This is not a valid number')
