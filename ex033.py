n1 = int(input('Type a number'))
n2 = int(input('Type a number'))
n3 = int(input('Type a number'))
if n1 > n2 and n1 > n3:
    print('The greatest number is {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('The greatest number is {}'.format(n2))
else:
    print('The greatest number is {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('The smallest number is {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('The smallest number is {}'.format(n2))
else:
    print('The smallest number is {}'.format(n3))
