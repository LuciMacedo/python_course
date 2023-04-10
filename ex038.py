num1 = int(input("Enter  a number: "))
num2 = int(input('Enter second number: '))

if num1 > num2:
    print('Number {} is greater than {}'.format(num1, num2))
elif num1 < num2:
    print('Number {} is greater than {}'.format(num2, num1))
else:
    print('The numbers are equal')