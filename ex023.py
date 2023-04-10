num = int(input('Type a number: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10
print('unit: {}, ten: {}, hundred: {}, thousand: {}'.format(uni, dez, cen, mi))

